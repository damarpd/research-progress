import pandas as pd

df = pd.read_csv("SLR-prior.csv")
keep = {"Key": "zotero_key", "Author": "authors", "Publication Year": "year",
        "Title": "title", "Publication Title": "venue", "DOI": "doi", "Date Added": "date_added"}
inv = df[list(keep)].rename(columns=keep).sort_values(["year", "authors"])

inv.insert(0, "id", [f"P{i:03d}" for i in range(1, len(inv) + 1)])  # P001, P002, ...
inv["found_via"] = ""     # supervisor / Google Scholar / citation / conference
inv["prior_use"] = ""     # e.g. cited in intro, methods reference, key finding
inv["on_topic"] = ""      # yes / uncertain (only for the benchmark split)

inv.to_excel("prior_inventory.xlsx", index=False)   # needs: pip install openpyxl
print(inv["doi"].isna().sum(), "articles missing a DOI")