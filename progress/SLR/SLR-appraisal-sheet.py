import os
import pandas as pd
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

OUT = "appraisal_sheet.xlsx"
ROWS = 200   # formulas and dropdowns are prepared for this many included studies

# one-time generator: rerunning would overwrite the scores typed in Excel
if os.path.exists(OUT):
    raise SystemExit(f"{OUT} already exists, not overwriting")

COLS = ["ft_id", "screen_id", "study", "title", "tier", "study_type",
        "Q1", "Q2", "Q3", "Q4", "Q5",
        "total", "applicable", "score_pct",
        "Q1_basis", "Q2_basis", "Q3_basis", "Q4_basis", "Q5_basis", "status"]

first = {
    "ft_id": "F001", "screen_id": "S094", "study": "Narendra et al. 2019",
    "title": "The modeling of dwelling time of buses at bus stop", "tier": "core",
    "study_type": "both", "Q1": 0.5, "Q2": 0.5, "Q3": 0.5, "Q4": 0.5, "Q5": 0.5,
    "Q1_basis": "video at 6 Trans Jogja stops, 7 days, 07:00-18:00, 172 bus-stop events, camera position given; stops not named, layout and the way counts and times were extracted not described",
    "Q2_basis": "n = 172 events from 6 stops (about 29 per stop), adequate for a simple regression; events treated as independent, no per-stop breakdown, light loads (mean 3.4 boarding), claim of a generic BRT model goes beyond the sample",
    "Q3_basis": "dwell time defined differently in the abstract (enter to leave) and the methods (door open to close); alighting, boarding and additional service times have no start and end events; x1 undefined; Table 2 component means sum to 13.6 s, total mean 13.25 s",
    "Q4_basis": "linear fits with R2 (alighting 0.86, boarding 0.90), p < 0.001, chi-square and scatter plots, all on the fitting data; no hold-out or cross-validation; no R2 for the additional-service model",
    "Q5_basis": "states the model is limited to Trans Jogja operations and needs calibration elsewhere; does not discuss low passenger volumes, one operator, no crowding or stop layout",
    "status": "draft (Claude), to confirm",
}
rows = [first] + [{} for _ in range(ROWS - 1)]
df = pd.DataFrame(rows, columns=COLS)

CHECKLIST = pd.DataFrame({
    "#": ["Q1", "Q2", "Q3", "Q4", "Q5"],
    "question": [
        "Is the data source described (observation method, location, duration)?",
        "Is the sample size reported and adequate for the claims made?",
        "Are the measures defined clearly (e.g. flow, density, speed, boarding/alighting time)?",
        "Was the model calibrated and validated against observed data?",
        "Are limitations reported?"],
    "applies to": ["all", "empirical studies", "all", "modeling and simulation studies", "all"],
})
GUIDE = ("Score each question: 1 = yes, 0.5 = partly, 0 = no, NA = not applicable "
         "(Q2 for pure models, Q4 for pure empirical studies). Scores describe the strength of evidence "
         "and are reported in the synthesis; they are not used to exclude studies (protocol section 7).")

with pd.ExcelWriter(OUT, engine="openpyxl") as w:
    df.to_excel(w, index=False, sheet_name="appraisal")
    ws = w.sheets["appraisal"]
    widths = {"A": 8, "B": 10, "C": 24, "D": 44, "E": 13, "F": 12, "G": 6, "H": 6, "I": 6, "J": 6, "K": 6,
              "L": 8, "M": 11, "N": 10, "O": 44, "P": 44, "Q": 44, "R": 44, "S": 44, "T": 24}
    for col, wd in widths.items():
        ws.column_dimensions[col].width = wd
    for cell in ws[1]:
        cell.font = Font(bold=True)
    for col in ["G", "H", "I", "J", "K"]:
        ws[f"{col}1"].fill = PatternFill("solid", fgColor="FFF2CC")
    for col in ["L", "M", "N"]:
        ws[f"{col}1"].fill = PatternFill("solid", fgColor="E2EFDA")
    for r in range(2, ROWS + 2):
        ws[f"L{r}"] = f'=IF(A{r}="","",SUM(G{r}:K{r}))'
        ws[f"M{r}"] = f'=IF(A{r}="","",COUNT(G{r}:K{r}))'
        ws[f"N{r}"] = f'=IF(OR(A{r}="",M{r}=0),"",L{r}/M{r})'
        ws[f"N{r}"].number_format = "0%"
        for cell in ws[r]:
            cell.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "E2"

    dv = DataValidation(type="list", formula1='"1,0.5,0,NA"', allow_blank=True, showErrorMessage=False)
    ws.add_data_validation(dv)
    dv.add(f"G2:K{ROWS + 1}")
    dv2 = DataValidation(type="list", formula1='"core,transferable"', allow_blank=True, showErrorMessage=False)
    ws.add_data_validation(dv2)
    dv2.add(f"E2:E{ROWS + 1}")
    dv3 = DataValidation(type="list", formula1='"empirical,modeling,both"', allow_blank=True, showErrorMessage=False)
    ws.add_data_validation(dv3)
    dv3.add(f"F2:F{ROWS + 1}")
    dv4 = DataValidation(type="list", formula1='"draft (Claude), to confirm,confirmed"', allow_blank=True, showErrorMessage=False)
    ws.add_data_validation(dv4)
    dv4.add(f"T2:T{ROWS + 1}")

    CHECKLIST.to_excel(w, index=False, sheet_name="checklist")
    wc = w.sheets["checklist"]
    wc.column_dimensions["A"].width = 6
    wc.column_dimensions["B"].width = 80
    wc.column_dimensions["C"].width = 32
    wc["A8"] = GUIDE
    wc["A8"].alignment = Alignment(wrap_text=True, vertical="top")
    wc.merge_cells("A8:C10")

print("appraisal sheet ready:", OUT, "| rows prepared:", ROWS, "| pre-filled: F001")
