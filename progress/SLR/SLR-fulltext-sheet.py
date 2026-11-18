import os
import pandas as pd
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

SEED = 20261118   # fixed so the pilot batch is reproducible
N_PILOT = 20
OUT = "fulltext_sheet.xlsx"

# the sheet is a one-time generator: rerunning would overwrite the decisions typed in Excel
if os.path.exists(OUT):
    raise SystemExit(f"{OUT} already exists, not overwriting")

s = pd.read_excel("screening_sheet.xlsx", sheet_name="screening")
keep = s[s["decision"].isin(["include", "maybe"])].copy()

# companion reports of the same study (conference version of a journal paper), counted once
COMPANION = {"S407": "S354", "S423": "S051"}
MAIN = {v: k for k, v in COMPANION.items()}
keep["duplicate_note"] = ""
for c, m in COMPANION.items():
    keep.loc[keep["screen_id"] == c, "duplicate_note"] = f"companion of {m}, count once"
    keep.loc[keep["screen_id"] == m, "duplicate_note"] = f"main study; companion {c}"

# pilot batch: 20 random records (not companions), read first to test the full-text criteria
pilot_ids = set(keep[~keep["screen_id"].isin(COMPANION)].sample(N_PILOT, random_state=SEED)["screen_id"])
keep["batch"] = keep["screen_id"].map(lambda x: "pilot" if x in pilot_ids else "main")

# order: pilot first, then core before transferable before untiered, then screening id
tier_rank = {"core": 0, "transferable": 1}
keep["_t"] = keep["tier_if_include"].map(tier_rank).fillna(2)
keep["_b"] = (keep["batch"] != "pilot").astype(int)
keep = keep.sort_values(["_b", "_t", "screen_id"]).reset_index(drop=True)
keep.insert(0, "ft_id", [f"F{i:03d}" for i in range(1, len(keep) + 1)])

sheet = pd.DataFrame({
    "ft_id": keep["ft_id"], "screen_id": keep["screen_id"], "batch": keep["batch"],
    "year": keep["year"], "title": keep["title"], "source": keep["source"], "doi": keep["doi"],
    "abstract_decision": keep["decision"], "abstract_tier": keep["tier_if_include"],
    "abstract_notes": keep["notes"], "duplicate_note": keep["duplicate_note"],
    "full_text_found": "", "ft_decision": "", "ft_reason_if_exclude": "", "ft_tier": "", "ft_notes": "",
    "abstract": keep["abstract"],
})

REASONS = [
    "full text not available",
    "no boarding/alighting analysis at a platform-vehicle interface",
    "none of the outcomes of interest reported (layout effect, crowd measure, movement model, boarding/alighting time)",
    "not a primary study (review, commentary, editorial)",
    "duplicate report of another included study",
    "insufficient detail to extract or appraise",
    "other",
]

with pd.ExcelWriter(OUT, engine="openpyxl") as w:
    sheet.to_excel(w, index=False, sheet_name="fulltext")
    ws = w.sheets["fulltext"]
    widths = {"A": 8, "B": 10, "C": 8, "D": 7, "E": 44, "F": 26, "G": 24, "H": 12, "I": 13,
              "J": 28, "K": 26, "L": 12, "M": 12, "N": 44, "O": 14, "P": 34, "Q": 90}
    for col, wd in widths.items():
        ws.column_dimensions[col].width = wd
    for cell in ws[1]:
        cell.font = Font(bold=True)
    for col in "LMNOP":
        ws[f"{col}1"].fill = PatternFill("solid", fgColor="FFF2CC")
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "F2"

    # reasons are longer than the 255-character limit of an inline dropdown, so they live on a second sheet
    pd.DataFrame({"full-text exclusion reasons": REASONS}).to_excel(w, index=False, sheet_name="lists")
    w.sheets["lists"].column_dimensions["A"].width = 100

    n = len(sheet) + 1
    lists = {"L": '"yes,no"', "M": '"include,exclude"', "N": f"=lists!$A$2:$A${len(REASONS) + 1}",
             "O": '"core,transferable"'}
    for col, formula in lists.items():
        dv = DataValidation(type="list", formula1=formula, allow_blank=True, showErrorMessage=False)
        ws.add_data_validation(dv)
        dv.add(f"{col}2:{col}{n}")

print(len(sheet), "records;", (sheet["batch"] == "pilot").sum(), "in the pilot batch, seed", SEED)
print(sheet["abstract_tier"].fillna("none").value_counts().to_dict())
