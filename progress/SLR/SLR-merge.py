import re
import pandas as pd

# Merge the Scopus and Web of Science exports of search string v0.3, remove duplicates,
# and flag which prior articles the search retrieved.

def norm_title(t):
    return re.sub(r"[^a-z0-9]", "", str(t).lower())

def norm_doi(x):
    return x.strip().lower() if isinstance(x, str) and x.strip() else None

sc = pd.read_csv("scopus_v03.csv", encoding="utf-8-sig")
wo = pd.read_csv("wos_v03.csv", encoding="utf-8-sig")

a = pd.DataFrame({
    "db": "Scopus", "title": sc["Title"], "authors": sc["Authors"], "year": sc["Year"],
    "source": sc["Source title"], "doi": sc["DOI"], "abstract": sc["Abstract"],
    "author_keywords": sc["Author Keywords"], "db_id": sc["Link"]})
b = pd.DataFrame({
    "db": "WoS", "title": wo["Article Title"], "authors": wo["Authors"], "year": wo["Publication Year"],
    "source": wo["Source Title"], "doi": wo["DOI"], "abstract": wo["Abstract"],
    "author_keywords": wo["Author Keywords"], "db_id": wo["UT (Unique WOS ID)"]})
allr = pd.concat([a, b], ignore_index=True)
allr["doi_n"] = allr["doi"].map(norm_doi)
allr["tkey"] = allr["title"].map(norm_title)

# union-find: link rows with the same DOI, or with the same normalized title when
# at least one of the two has no DOI
parent = list(range(len(allr)))
def find(i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i
def union(i, j):
    parent[find(i)] = find(j)

for _, g in allr[allr.doi_n.notna()].groupby("doi_n"):
    idx = list(g.index)
    for j in idx[1:]:
        union(idx[0], j)
for _, g in allr.groupby("tkey"):
    idx = list(g.index)
    for x in range(len(idx)):
        for y in range(x + 1, len(idx)):
            i, j = idx[x], idx[y]
            if pd.isna(allr.at[i, "doi_n"]) or pd.isna(allr.at[j, "doi_n"]) or allr.at[i, "doi_n"] == allr.at[j, "doi_n"]:
                union(i, j)
allr["cluster"] = [find(i) for i in range(len(allr))]

rows = []
for _, g in allr.groupby("cluster", sort=False):
    g = g.sort_values("db", key=lambda s: s.map({"Scopus": 0, "WoS": 1}))
    first = g.iloc[0]
    abstract = next((x for x in g["abstract"] if isinstance(x, str) and x.strip()), None)
    keywords = next((x for x in g["author_keywords"] if isinstance(x, str) and x.strip()), None)
    doi = next((x for x in g["doi"] if isinstance(x, str) and x.strip()), None)
    rows.append({
        "title": first["title"], "authors": first["authors"], "year": first["year"],
        "source": first["source"], "doi": doi, "abstract": abstract, "author_keywords": keywords,
        "found_in": "+".join(sorted(set(g["db"]), key=lambda s: ["Scopus", "WoS"].index(s))),
        "n_records": len(g),
        "scopus_link": next((x for x, d in zip(g["db_id"], g["db"]) if d == "Scopus"), None),
        "wos_ut": next((x for x, d in zip(g["db_id"], g["db"]) if d == "WoS"), None),
        "_doi_n": norm_doi(doi), "_tkey": norm_title(first["title"]),
    })
m = pd.DataFrame(rows).sort_values(["year", "title"]).reset_index(drop=True)
m.insert(0, "rec_id", [f"R{i:04d}" for i in range(1, len(m) + 1)])

# flag prior articles retrieved by the search
inv = pd.read_excel("prior_inventory.xlsx")
inv["_doi_n"] = inv["doi"].map(norm_doi)
inv["_tkey"] = inv["title"].map(norm_title)
m["prior_id"] = ""
prior_rows = []
for _, p in inv.iterrows():
    hit = m[(m["_doi_n"] == p["_doi_n"]) | (m["_tkey"] == p["_tkey"])]
    if len(hit):
        m.loc[hit.index, "prior_id"] = p["id"]
    prior_rows.append((p["id"], p["on_topic"], "retrieved" if len(hit) else "NOT retrieved",
                       hit.iloc[0]["found_in"] if len(hit) else "", hit.iloc[0]["rec_id"] if len(hit) else ""))

m.drop(columns=["_doi_n", "_tkey"]).to_csv("merged_v03.csv", index=False, encoding="utf-8-sig")

n_sc, n_wo = len(a), len(b)
print(f"Scopus records: {n_sc}")
print(f"Web of Science records: {n_wo}")
print(f"Total identified: {n_sc + n_wo}")
print(f"Unique records after deduplication: {len(m)}")
print(f"Duplicates removed: {n_sc + n_wo - len(m)}")
print(m["found_in"].value_counts().to_string())
print("\nPrior articles:")
print(pd.DataFrame(prior_rows, columns=["id", "on_topic", "search", "found_in", "rec_id"]).to_string(index=False))
