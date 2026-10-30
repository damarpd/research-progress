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
| Scopus | 23/10/2026 | 2178 | 5 of 5: P001, P004, P009, P010, P012 | +791 hits (+57%) versus v0.1 |
| Web of Science | 23/10/2026 | 902 | 5 of 5: P001, P004, P009, P010, P012 | Core Collection; add the editions searched |

Note on validity: v0.2 was revised after seeing which validation paper v0.1 missed (P004), so the 5 of 5 is no longer a fully blind test. Report v0.1 (4 of 5, before revision) and v0.2 (5 of 5, after revision) together.

Expected effect: more hits than v0.1 because `bus` and the added block C terms are broad. If the count rises sharply, tighten with proximity (for example `bus W/5 board*`) before considering any subject-area filter.

### Scopus export of v0.2 and precision check

- Export: `scopus_v02.csv`, exported on 26/10/2026, 2180 records (the count shown earlier was 2178; Scopus re-indexes between runs). Fields: title, abstract, authors, year, source, DOI, author keywords, document type. 239 records have no DOI; 15 titles are duplicated within the export.
- Precision sample: `precision_sample.xlsx`, 50 records drawn at random from the export with seed 20261026 (`SLR-precision-sample.py`), judged from title and abstract against protocol section 5.

| judgement | records |
|---|---|
| relevant | 5 |
| maybe | 6 |
| not relevant | 39 |

- Precision: 5/50 = 10% counting "relevant" only (about 4-21%), and 11/50 = 22% with "maybe" (about 13-35%). Intervals are approximate (Wilson, 95%).
- Reasons for "not relevant": about 32 of 39 come from non-transport engineering (electronics, robotics, aerospace, communications, batteries, signal processing). About 7 are transport papers outside the topic (metro station clustering, shuttle dispatching, bus line optimization, BRT corridor selection). The noise comes from generic terms that mean something else in engineering: `bus` (data bus), `board*` (circuit board, on-board), `platform*` (hardware platform), and to a lesser degree `trajector*`, `layout*`, `queu*`.
- S48 (light rail passenger flow estimation) was first judged relevant, then changed to maybe after a second look. S45 (camera tracking of passengers during bus boarding) stays relevant.
- Benchmark coverage in the v0.2 export: 9 of the 10 benchmark papers are present. P011 (keyword half, borderline yes) is not in the export. Confirmed in Scopus (date to add): P011 is indexed (found by DOI alone) but is not retrieved when its DOI is combined with the v0.2 search. The likely cause is that its abstract contains no boarding or alighting wording (block B). Decision: accept the miss, leave the string unchanged, and let P011 enter through the "other methods" route.
- Approximate test of a tighter string on the export (text match on title, abstract and author keywords only, not a Scopus run): about 489 of 2180 records remain; all 5 relevant sample records, 4 of 6 maybe (S27 bus bunching and S43 level boarding accessibility are lost) and 4 of 39 irrelevant records are kept; all 9 benchmark papers in the export are kept.

## Version 0.3 (draft, not yet run)

- Reason: the precision check of v0.2 showed that most noise comes from generic terms in blocks A and B.
- Changes from v0.2:
    - block A: removed bare `bus` and `platform*`; added `"bus passenger*"`, `"bus dwell time"`, `"station platform*"`, `"train platform*"`, `"metro platform*"`, `"subway platform*"`, `"rail platform*"`, `"transit platform*"`, `"platform edge door*"`, `"train door*"`
    - block B: `boarding` OR `alight*` OR `"board and alight*"` OR `"train door*"`; removed bare `board*`
    - block C: unchanged
- Filters unchanged: 2000-2026, English, journal articles and conference papers.

**Scopus**

```
TITLE-ABS-KEY(
  ( "bus rapid transit" OR BRT OR busway* OR "bus station*" OR "bus stop*"
    OR "bus platform*" OR "bus passenger*" OR "bus dwell time"
    OR "public transport*" OR "transit station*"
    OR metro OR subway OR "urban rail" OR "rail transit" OR "metro station*"
    OR "train station*" OR "station platform*" OR "train platform*"
    OR "metro platform*" OR "subway platform*" OR "rail platform*"
    OR "transit platform*" OR "platform edge door*" OR "train door*" )
  AND
  ( boarding OR alight* OR "board and alight*" OR "train door*" )
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

**Web of Science:** `TS=( same three blocks )`, with the same filters as v0.2.

| database | date run | hits | benchmark papers retrieved | notes |
|---|---|---|---|---|
| Scopus | 26/10/2026 | 515 | 9 of 9: P001, P004, P005, P006, P008, P009, P010, P012, P015 | 76% fewer hits than v0.2 (2180); P011 is a known miss |
| Web of Science | 26/10/2026 | 366 | 9 of 9: P001, P004, P005, P006, P008, P009, P010, P012, P015 | Core Collection; add the editions searched; P011 is a known miss |

After running: check all benchmark papers (validation half P001, P004, P009, P010, P012 and keyword half P005, P006, P008, P015; P011 is a known miss), then draw a new, smaller precision sample from the v0.3 results.

### Scopus export of v0.3 and precision check

- Export: `scopus_v03.csv`, 515 records, all English, years 2000-2026; 23 records have no DOI; all 9 retrievable benchmark papers are present. 508 of the 515 records are also in the v0.2 export. The export has no document type column (the search filter handled it).
- Precision sample: `precision_sample_v03.xlsx`, 50 records drawn at random with seed 20261027 (`SLR-precision-sample-v03.py`), judged from title and abstract against protocol section 5. Four "relevant" judgements (T14, T19, T22, T26) were reread afterwards; T14 and T19 changed to maybe.

| judgement | records | v0.2 sample for comparison |
|---|---|---|
| relevant | 16 | 5 |
| maybe | 20 | 6 |
| not relevant | 14 | 39 |

- Precision: 16/50 = 32% counting "relevant" only (about 21-46%), and 36/50 = 72% with "maybe" (about 58-83%). For v0.2 these were 10% and 22%. Intervals are approximate (Wilson, 95%).
- Reasons for "not relevant": all 14 are transport papers outside the topic (bus demand, reliability, route choice, travel time, fare collection, taxi services, service perception, metro clustering). The non-transport engineering noise seen in v0.2 (electronics, robotics, aerospace) is gone.
- No clearly BRT-specific study appears in the sample; the BRT coverage check is still open.
- Decision: v0.3 is accepted as the search string, pending the BRT coverage check.

### Web of Science export of v0.3

- Export: `wos_v03.csv`, 367 records (the count shown in the interface was 366; Web of Science updates between a search and an export). Custom selection: authors, title, source, abstract, document type, keywords, language. 367 records, all English, no duplicate WoS IDs or DOIs; 6 records have no DOI and 1 has no abstract. All 9 retrievable benchmark papers are present.
- One record has publication year 2027 ("Demand-driven urban rail transit timetabling: Research perspectives"); it is an early-access article of October 2026 whose volume year is 2027. It is kept as inside the 2000-2026 range.

### Merge and deduplication of the v0.3 exports (PRISMA identification numbers)

- Script: `SLR-merge.py`; output: `merged_v03.csv`. Records are matched by DOI, and by normalized title when at least one of the two records has no DOI.

| step | records |
|---|---|
| Scopus | 515 |
| Web of Science | 367 |
| total identified | 882 |
| duplicates removed | 281 |
| unique records to screen | 601 |

- Unique records by source: 279 in both databases, 234 in Scopus only, 88 in Web of Science only.
- Prior articles: 9 of the 10 on-topic prior articles were retrieved by the search (P001, P004, P005, P006, P008, P009, P010, P012, P015). P011 was not retrieved and enters through "other methods". The five prior articles judged not on topic (P002, P003, P007, P013, P014) were not retrieved, as expected.

### BRT coverage check (broad BRT query against v0.3)

- No known BRT papers were available, so a deliberately broad BRT query was run and compared with v0.3. Broad query: (`"bus rapid transit"` OR `BRT` OR `busway*`) AND (boarding OR `alight*` OR `board*` OR `"dwell time"` OR `"passenger service time"` OR `platform*` OR `"bus station*"` OR `"station design"` OR `"boarding time"`), with the same filters as v0.3 (2000-2026, English, articles and conference papers).

| database | date run | broad BRT query | also retrieved by v0.3 | not retrieved by v0.3 |
|---|---|---|---|---|
| Scopus | 26/10/2026 | 331 | 33 | 298 |
| Web of Science | 26/10/2026 | 179 | 16 | 163 |

- The records not retrieved by v0.3 are not yet judged. The broad query is noisy (`board*`, `platform*`, BRT as an acronym in other fields), so the counts alone do not measure recall. Next step: judge a random sample of the Scopus 298 against protocol section 5 and record how many are relevant and why v0.3 missed them.
- Sample: `brt_missed_sample.xlsx`, 50 records drawn at random from `scopus_brt_missed.csv` (298 records) with seed 20261028 (`SLR-brt-sample.py`), judged from title and abstract against protocol section 5.
- Result: 0 relevant, 0 maybe, 50 not relevant. Reasons: 26 no platform-level boarding/alighting, 13 BRT planning or operations only, 10 not transport (other meaning of BRT), 1 other.
- Reading: with 0 of 50, at most about 7% of the 298 missed records (about 21 papers) are likely to be relevant (95% upper bound), and the best estimate is close to zero. v0.3 is not losing relevant BRT papers in Scopus. The Web of Science misses (163 records) were checked afterwards, see below. The BRT papers v0.3 does retrieve (33 in Scopus, 16 in Web of Science) are the core-tier candidates and go to screening.
- Decision: v0.3 is frozen as the final search string. No BRT terms are added.
- Web of Science misses: the broad BRT query minus v0.3 gave 163 records (`wos_brt_missed.csv`). Of these, 2 are already in the merged set (retrieved by Scopus v0.3) and 146 are in the Scopus broad-BRT missed set (the population sampled above); the remaining 15 were missed by both databases (`brt_wos_remainder.xlsx`, `SLR-wos-brt-remainder.py`). All 15 were judged from title and abstract: 0 relevant, 0 maybe, 15 not relevant (4 other, 4 other meaning of BRT, 4 transit but not BRT platform, 3 no platform-level boarding/alighting).
- Conclusion: no relevant BRT paper was found among the records missed by v0.3 in either database. The v0.3 decision stands.

## Title/abstract screening: decisions and exclusion reasons

- Date logged: 27/10/2026, before screening starts. Sheet: `screening_sheet.xlsx` (601 unique records, random order, seed 20261030, prior flags and database hidden; key in `screening_key.csv`).
- Decision for each record: **include** (meets the criteria), **maybe** (cannot be decided from the abstract; goes to full text) or **exclude** (with one reason from the list below). For includes, record the tier: core (BRT) or transferable (metro, rail, bus).
- Screening question (protocol section 5): does the study examine boarding or alighting at a platform-vehicle interface (layout, doors, platform, crowd dynamics, boarding or alighting time, or a movement model)?
- Exclusion reasons (fixed list, one per excluded record; reason 7 was added on 30/10/2026 with protocol v0.4, before any record was judged):

| # | reason | use when |
|---|---|---|
| 1 | not boarding/alighting at a platform-vehicle interface | transport study, but boarding or alighting at the platform or door is not examined |
| 2 | in-vehicle crowding only | crowding or comfort inside the vehicle, without the platform-vehicle interaction |
| 3 | demand or route choice or station location only | demand forecasting, route or mode choice, network or station planning |
| 4 | operations or timetabling or bunching only | scheduling, headway, bunching or fleet operations without platform-level boarding analysis |
| 5 | general pedestrian or crowd flow without platform-level boarding | general pedestrian or crowd studies, including general fundamental diagrams, outside the boarding/alighting context |
| 6 | not transport or other field | electronics, robotics, medicine or another meaning of BRT or platform |
| 7 | review article (secondary study) | literature review, systematic review or survey of the literature (protocol v0.4, 30/10/2026); if relevant to the topic, write "review, keep for snowballing" in the notes column |
| 8 | other | any other reason; explain in the notes column |

- Not recorded as reasons because the search filters already handled them: language (English only), year (2000-2026), and document type (articles and conference papers). Records without full text are excluded at the full-text stage.
- Reasons feed the PRISMA 2020 flow diagram: the counts per reason are reported at the full-text stage, and the title/abstract stage reports the number of excluded records.
