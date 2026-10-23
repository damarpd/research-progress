import random
import pandas as pd

SEED = 20261023   # fixed so the split is reproducible; do not change after the split is committed

inv = pd.read_excel("prior_inventory.xlsx")
ids = sorted(inv.loc[inv["on_topic"] == "yes", "id"])   # 12 benchmark candidates

keyword_half = sorted(random.Random(SEED).sample(ids, len(ids) // 2))
split = pd.DataFrame({"id": ids})
split["half"] = split["id"].map(lambda i: "keyword" if i in keyword_half else "validation")
split.insert(1, "zotero_key", split["id"].map(inv.set_index("id")["zotero_key"]))
split["seed"] = SEED

split.to_csv("benchmark_split.csv", index=False)
print(split["half"].value_counts().to_string())
