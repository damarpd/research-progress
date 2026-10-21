# SLR protocol: platform layout and boarding/alighting dynamics at multi-berth BRT stations

- status: DRAFT (Steps 1-2 in progress, not registered)
- version: 0.3
- date: 2026-10-21
- guideline: Systematic Literature Review Guide: Boarding & Alighting at BRT Stations (PRISMA 2020 reporting, Wohlin 2014 snowballing)
- change log: record every change to this protocol below, with date and reason

| version | date | change |
|---|---|---|
| 0.1 | 2026-10-21 | first draft of PICOC, research questions, scope and eligibility criteria |
| 0.2 | 2026-10-21 | confirmed date range 2000-2026; databases Scopus and Web of Science (TRID dropped); added exclusion of pedestrian/crowd-flow studies without platform-level boarding/alighting |
| 0.3 | 2026-10-21 | quality appraisal set to a custom 5-question checklist; OSF registration skipped at this stage |

## 1. Background and aim

Boarding and alighting at stops and stations is a critical determinant of public transport service efficiency. At multi-berth BRT stations, platform layout is an open design question. The dissertation investigates how platform design affects boarding and alighting dynamics at multi-berth BRT stations (shared versus direction-separated layouts, from surveillance video within a fundamental diagram framework) and develops a passenger movement model for design and policy recommendations.

This SLR establishes what is already known and what is missing. It does not replace the empirical study. The link between boarding/alighting time and bus bunching is background for the introduction and is outside the scope of this review.

## 2. PICOC

| Element | Definition |
|---|---|
| **Population** | Passengers boarding and alighting at public transport platforms; multi-berth BRT stations are the target |
| **Intervention / exposure** | Platform design and layout: shared versus direction-separated boarding/alighting flows, berth configuration, door and platform geometry |
| **Comparison** | Layout alternatives, single-berth versus multi-berth platforms, crowd levels, and other modes (metro, bus) in the transferable tier |
| **Outcomes** | Crowd dynamics (flow, density, speed, fundamental diagram), boarding/alighting time, dwell time, conflicts |
| **Context** | BRT stations (core tier) and metro/bus platform-vehicle interfaces (transferable tier); studies using video or vision-based observation, experiments and simulation |

## 3. Research questions

- **RQ1 (layout):** How does platform layout, such as shared versus direction-separated flows and berth configuration, affect passenger boarding and alighting performance at BRT stations and comparable transit platforms?
- **RQ2 (crowd dynamics):** What crowd-dynamic characteristics of boarding and alighting have been established, especially through fundamental diagrams, and how were they measured from surveillance video or other observation?
- **RQ3 (modeling):** Which passenger movement models (microscopic, fundamental-diagram-based, macroscopic) have been used for boarding/alighting and platform design, and how were they calibrated and validated?
- **RQ4 (gap):** What gaps remain for multi-berth BRT platforms, in particular layout comparisons supported by empirical video data? RQ4 is answered by synthesis of RQ1-RQ3, not by a separate search.

## 4. Scope: two tiers

- **Core tier:** studies set in BRT stations or busway platforms.
- **Transferable tier:** studies of metro, rail or conventional bus platform-vehicle interfaces. Included only if they examine the boarding/alighting interaction at the platform (layout, doors, flow separation, crowd dynamics), and analyzed separately from the core tier.
- Reason: BRT-specific literature is expected to be thin, and most of the pre-search corpus is metro-based (see section 8).

## 5. Eligibility criteria (draft, to be confirmed)

**Include**
- peer-reviewed journal articles and conference papers
- empirical, experimental, simulation or modeling studies of boarding and alighting at a platform-vehicle interface
- studies reporting at least one of: layout or design effect, crowd-dynamic measures (flow, density, speed, fundamental diagram), movement or process model, or boarding/alighting time
- English language
- publication year 2000-2026

**Exclude**
- in-vehicle comfort or crowding only, without platform-vehicle interaction
- route choice, demand forecasting or station location without platform-level interaction
- operational studies of bunching or headway without platform-level boarding/alighting analysis
- pedestrian or crowd-flow studies (including general fundamental diagrams) without platform-level boarding/alighting analysis
- editorials, commentaries, theses without peer review, and records with no full text available

## 6. Information sources

- Scopus and Web of Science as main sources (TRID not used)
- Google Scholar as a supplement only (first 200 results)
- snowballing from included studies (backward and forward)
- for every search, record date, exact string, filters and hit count in the search log

## 7. Selection, appraisal, extraction and synthesis

- screening: title/abstract, then full text, with exclusion reasons recorded; a second reviewer screens a 10-20% random sample and kappa is reported
- quality appraisal: one custom checklist applied to every included study (see below)
- extraction form: to be piloted on 3-5 papers
- synthesis: descriptive mapping and thematic synthesis, analyzed separately for core and transferable tiers; PRISMA 2020 flow diagram

### Quality appraisal checklist

Each question is scored yes (1), partly (0.5), no (0) or not applicable. The same checklist is applied to all included studies, prior or new. Scores describe the strength of evidence and are reported in the synthesis; they are not used to exclude studies.

| # | question | applies to |
|---|---|---|
| Q1 | Is the data source described (observation method, location, duration)? | all |
| Q2 | Is the sample size reported and adequate for the claims made? | empirical studies |
| Q3 | Are the measures defined clearly (e.g. flow, density, speed, boarding/alighting time)? | all |
| Q4 | Was the model calibrated and validated against observed data? | modeling and simulation studies |
| Q5 | Are limitations reported? | all |

## 8. Handling of previously found articles

- 15 prior articles were inventoried and frozen on 2026-10-05 (`progress/SLR/prior_inventory.xlsx`, commits `cf3cbca` and `6c88a19`).
- Their `on_topic` labels (7 yes, 8 uncertain) were assigned before these criteria existed. They are used only to choose the benchmark set. The 8 uncertain papers will be re-judged against section 5.
- Prior articles never bypass the search. They are used for validation of the search string, enter through the "other methods" route if the search misses them, and are screened and appraised with the same criteria as every other record.
- Validation: on-topic prior articles are split randomly with a fixed seed into a keyword half and a hidden half. Recall of the final search string is reported on the hidden half as a count.

## 9. Open decisions

- [x] date range 2000-2026 and English only (decided 2026-10-21)
- [x] databases: Scopus and Web of Science (decided 2026-10-21)
- [x] studies without platform-level boarding/alighting analysis are excluded, including general fundamental-diagram studies (decided 2026-10-21)
- [x] quality appraisal: custom checklist (decided 2026-10-21)
- [x] OSF registration: skipped at this stage (decided 2026-10-21); revisit before running the searches if the supervisor asks for it

## 10. Additional notes (you can avoid this subsection)
- Consideration of deciding the date range 
    - first BRT was introduced/ implemented in Curitiba, Brazil in 1974
    - TransMilenio breakthrough was introduced in 2000
    - TransJakarta was introduced in 2004