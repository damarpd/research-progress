# SLR search log

Protocol: `protocol.md` v0.3. Every version of the search string is recorded here with its date, filters and hit counts, as required by PRISMA 2020 (items 6 and 7).

## Benchmark split

- `benchmark_split.csv`, made by `SLR-split.py` with seed 20261023 on 2026-10-23.
- Keyword half (used to mine terms): P002, P005, P006, P008, P011, P015.
- Validation half (hidden, used only to test recall): the other six on-topic prior articles. Do not read them for keywords.
- Author keywords are not in the Zotero export (tags only hold "prior"), so terms were taken by hand from the titles and abstracts of the keyword half.

## Terms mined from the keyword half

| block | term | source |
|---|---|---|
| A context | platform | P005, P006, P008, P015 |
| A context | metro, metro station, urban rail, rail transit, train | P005, P006, P008, P011, P015 |
| A context | bus rapid transit, BRT, busway, bus station | not in keyword half; added from PICOC and the protocol |
| B process | boarding, alighting, board and alight | P005, P006, P008, P015 |
| B process | dwell time | P006 |
| B process | passenger service time (PST) | P005 |
| B process | train door | P006, P008, P015 |
| C design and dynamics | fundamental diagram | P002, P011 |
| C design and dynamics | crowd dynamics, pedestrian dynamics | P002, P008 |
| C design and dynamics | bottleneck, bi-directional flow | P002, P008 |
| C design and dynamics | time headway | P008 |
| C design and dynamics | social force model | P015 |
| C design and dynamics | level of service | P005 |
| C design and dynamics | pedestrian traffic management, keep out zone, differentiated doors | P005 |
| C design and dynamics | door width, platform edge doors, horizontal gap | P006 |
| C design and dynamics | queuing, waiting behavior | P015 |
| C design and dynamics | trajectories, surveillance video | P002, P008 |

## Version 0.1 (draft, not yet run)

- Date drafted: 2026-10-23
- Concept blocks: A context AND B process AND C design and dynamics. Outcomes are not searched.
- Filters: 2000-2026, English, journal articles and conference papers.

**Scopus**

```
TITLE-ABS-KEY(
  ( "bus rapid transit" OR BRT OR busway* OR "bus station*" OR "bus platform*"
    OR metro OR subway OR "urban rail" OR "rail transit" OR "metro station*"
    OR "train station*" OR platform* )
  AND
  ( board* OR alight* OR "dwell time" OR "passenger service time" OR "train door*" )
  AND
  ( "fundamental diagram*" OR "crowd dynamic*" OR "pedestrian dynamic*" OR bottleneck*
    OR bidirectional OR bi-directional OR "time headway" OR "social force"
    OR "level of service" OR "door width" OR "platform edge door*" OR "keep out zone"
    OR "differentiated door*" OR queu* OR "waiting behavio*" OR trajector*
    OR "surveillance video" OR layout* OR "flow separat*" )
)
AND PUBYEAR > 1999 AND PUBYEAR < 2027
AND LANGUAGE( english )
AND ( DOCTYPE( ar ) OR DOCTYPE( cp ) )
```

**Web of Science:** `TS=( same three blocks )`, with filters publication years 2000-2026, language English, document types Article and Proceedings Paper.

| database | date run | hits | hidden papers retrieved (of 6) | notes |
|---|---|---|---|---|
| Scopus | not run | | | |
| Web of Science | not run | | | |

Known risks of v0.1: `board*` also matches unrelated words (boarder, boardroom); `platform*` also matches software platforms; `metro` and `queu*` may add noise. Block C is the widest block, so check the first 50-100 results for off-topic papers.
