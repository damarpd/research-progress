# SLR search log

Protocol: `protocol.md` v0.3. Every version of the search string is recorded here with its date, filters and hit counts, as required by PRISMA 2020 (items 6 and 7).

## Benchmark split

- `benchmark_split.csv`, made by `SLR-split.py` with seed 20261023 on 2026-10-23.
- Keyword half (used to mine terms): P002, P005, P006, P008, P011, P015.
- Validation half (hidden, used only to test recall): the other six on-topic prior articles. Do not read them for keywords.
- Author keywords are not in the Zotero export (tags only hold "prior"), so terms were taken by hand from the titles and abstracts of the keyword half.

## Benchmark re-judging after the first search

- The first search (v0.1) missed P004 and P013. P013 had no boarding/alighting content, so all seven original "yes" papers (labelled before the protocol existed) were re-judged against protocol section 5, whether or not they had been retrieved. This happened after the first search and is recorded as a deviation. Sheet: `original_yes_rejudge.xlsx`.
- Result: P002 and P013 changed to "no"; P008, P009, P010, P011 and P015 stay "yes". P009 and P011 were borderline and kept.
- The split in `benchmark_split.csv` is unchanged. The effective benchmark is the papers with `on_topic` = yes in the inventory (10):
    - keyword half (5): P005, P006, P008, P011, P015
    - validation half (5): P001, P004, P009, P010, P012
- Recall of v0.1 on the effective validation half: 4 of 5 (P001, P009, P010, P012 retrieved; P004 missed). On the original six it was 4 of 6.

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
| Scopus | 23/10/2026 | 1387 | 4 of 6: P001, P009, P010, P012 retrieved; P004 and P013 missed | saved search `brt_v01` |
| Web of Science | not run | | | |

Known risks of v0.1: `board*` also matches unrelated words (boarder, boardroom); `platform*` also matches software platforms; `metro` and `queu*` may add noise. Block C is the widest block, so check the first 50-100 results for off-topic papers.

## Version 0.2 (draft, not yet run)

- Date drafted: see commit date
- Reason: v0.1 missed P004 (bus boarding and alighting dynamics, smart card data). Its abstract has no term from block A beyond "bus" and none from block C. The changes generalize the context and outcome vocabulary and are not tailored to P004 alone. P013 was a correct miss and is not a reason for change.
- Changes from v0.1:
    - block A: added `bus`, `"bus stop*"`, `"public transport*"`, `"transit station*"`
    - block B: `board*`, `alight*`, `"train door*"` only; `"dwell time"` and `"passenger service time"` moved to block C so that a paper must mention boarding or alighting
    - block C: added `"dwell time"`, `"passenger service time"`, `"boarding time"`, `"alighting time"`, `"passenger flow"`
- Filters unchanged: 2000-2026, English, journal articles and conference papers.

**Scopus**

```
TITLE-ABS-KEY(
  ( "bus rapid transit" OR BRT OR busway* OR bus OR "bus station*" OR "bus stop*"
    OR "bus platform*" OR "public transport*" OR "transit station*"
    OR metro OR subway OR "urban rail" OR "rail transit" OR "metro station*"
    OR "train station*" OR platform* )
  AND
  ( board* OR alight* OR "train door*" )
  AND
  ( "fundamental diagram*" OR "crowd dynamic*" OR "pedestrian dynamic*" OR bottleneck*
    OR bidirectional OR bi-directional OR "time headway" OR "social force"
    OR "level of service" OR "door width" OR "platform edge door*" OR "keep out zone"
    OR "differentiated door*" OR queu* OR "waiting behavio*" OR trajector*
    OR "surveillance video" OR layout* OR "flow separat*"
    OR "dwell time" OR "passenger service time" OR "boarding time"
    OR "alighting time" OR "passenger flow" )
)
AND PUBYEAR > 1999 AND PUBYEAR < 2027
AND LANGUAGE( english )
AND ( DOCTYPE( ar ) OR DOCTYPE( cp ) )
```

**Web of Science:** `TS=( same three blocks )`, with the same filters as v0.1.

| database | date run | hits | validation papers retrieved (of 5: P001, P004, P009, P010, P012) | notes |
|---|---|---|---|---|
| Scopus | (add date) | 2178 | 5 of 5: P001, P004, P009, P010, P012 | +791 hits (+57%) versus v0.1 |
| Web of Science | | | | |

Note on validity: v0.2 was revised after seeing which validation paper v0.1 missed (P004), so the 5 of 5 is no longer a fully blind test. Report v0.1 (4 of 5, before revision) and v0.2 (5 of 5, after revision) together.

Expected effect: more hits than v0.1 because `bus` and the added block C terms are broad. If the count rises sharply, tighten with proximity (for example `bus W/5 board*`) before considering any subject-area filter.
