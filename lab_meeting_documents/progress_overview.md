# Public Transit User Dynamics: A Simulation Framework Under Crowding Situation in [location] Context


## Introduction

### Background study

<u>General problem</u>

Rapid urbanization has become a defining feature of modern cities. To facilitate daily mobility for various trip purposes, such as commuting to work and school, the use of public transportation has been increasingly promoted. This trend has led to a growing demand for public transport systems, particularly metro rail and city bus services, within urban contexts. During off-peak hours, operational issues such as delays are relatively uncommon. However, as passenger demand intensifies during peak periods, such issues become more prevalent. In particular, critical processes such as passenger movement/dynamics within alighting and boarding during the public transport operations can serve as key contributors to these delays. During peak hours, congestion on both platforms and inside trains often forces passengers to wait for multiple trains before they are able to board, and the longer this wait becomes, the stronger the time pressure passengers experience to complete their trip on time; under sufficiently high time pressure, passengers tend to shift from conservative, rule-following behavior toward more radical, competitive behavior, which can escalate into conflicts at the train door ([Qu et al., 2019](https://doi.org/10.1016/j.physa.2019.121075)). This time pressure is further amplified by an asymmetry in the consequences of missing the door: a boarding passenger who misses the door merely waits for the next train at the same station, whereas an alighting passenger who misses the door must travel to the next station and return, incurring a substantially higher cost ([Qu et al., 2019](https://doi.org/10.1016/j.physa.2019.121075)). This asymmetry explains why alighting passengers tend to exhibit greater urgency than boarding passengers, moving faster and more consistently throughout the alighting process ([Qu et al., 2019](https://doi.org/10.1016/j.physa.2019.121075)), illustrating how individual passenger behavior at the platform-train interface can directly shape the efficiency of the boarding and alighting process.

Alighting and boarding process is one of critical process in public transport operation. This kind of specific process has been extensively modeled by various approaches with passenger as a key player/agents involve in alighting and boarding process. These approaches cover social force model approach ([Yining Jia, et.al.,2026](https://doi.org/10.1016/j.physa.2026.131279), [Shen et.al., 2026](https://doi.org/10.1016/j.simpat.2026.103260), [Li et.al., 2020](https://doi.org/10.1016/j.tra.2019.12.017)), Markov process ([Baali et.al., 2025](https://doi.org/10.1016/j.physa.2025.130942)). 

Additionally, in the methodological area of microscopic pedestrian modelling, [Chen,Xu, et.al, (2017)](https://doi.org/10.1080/01441647.2017.1396265) classified pedestrian dynamics models into two primary categories namely continuous model and discrete-based model. 


<u>Rationale of the study</u>


Most prior studies have primarily focused on passenger movements associated with entering and exiting vehicles during boarding and alighting processes ([Qu Y., et.al.,2019](https://doi.org/10.1016/j.physa.2019.121075), [Seriani and Fernandez, 2015](https://doi.org/10.1016/j.trc.2015.02.003)). In contrast, at this moment, only [Yining Jia, et.al.(2026)](https://doi.org/10.1016/j.physa.2026.131279) explicitly consider a categorization of metro passengers into three groups—boarding, alighting, and remaining on-board passengers. However, their analysis is situated within normal operating conditions, where remaining passengers are typically seated, as supported by controlled experimental settings by [Fu L., et.al., 2023](https://doi.org/10.1016/j.tust.2023.105362). This limits the applicability of existing findings to more complex and crowded real-world contexts.

The focus of this study is alighting and boarding process when public transport facing crowded situation. Individual interactions between passengers during the crowded situation might affect the operation such as dwelling time. Passengers might act different behavior during the boarding and alighting process. Aligned with previous study, the behavior of each pedestrian is different, since it severely influences the movement characteristics, thus, developing crowd model by implementing multiple pedestrian classes is essential ([Duives D.C.,Daamen W., Hoogendoorn S.P., 2013](https://doi.org/10.1016/j.trc.2013.02.005)). Accordingly, this study proposes multiple pedestrian type, that might have different type of behavior during boarding and alighting process, to be considered to the further examination of pedestrian dynamics. The passenger type can be separated into two categories of the state, namely non-stationary and stationary. 

Regarding the approach to model pedestrian dynamics, [Seriani and Fernandez, (2015)](https://doi.org/10.1016/j.trc.2015.02.003) argued that continuous movement on pedestrian dynamics modelling ensure more realistic representations as the space is free from artificial restrictions, such as cells or grids in Cellular Automata approach. However, continuous model seem to be able to reproduce pedestrian movement, but the movements of the pedestrians are not directly related to decision-making processes of pedestrians ([Asano, Iryo & Kuwahara, 2009](https://link.springer.com/chapter/10.1007/978-1-4419-0820-9_28)). Additionally, besides the decision processes of *individual pedestrians* is essential to model such situation, the decision processes of *pedestrians interacting with each other* should be considered to reproduce pedestrian flow, such as during the congested situations. 

The passenger category, during the boarding and alighting process, depends on each state, are described as follows:

 |State|Type|Represented by|
 |-----|----|--------------|
 |Non-stationary|Passenger alighting|$(PA_{m})$|
 ||Passenger boarding |$(PB_{m})$|
 |Stationary|Passenger stay inside the car |$(PC_{s})$|
 ||Passenger stay on the platform waiting for boarding process |$(PP_{s})$|

<u>Research objective</u>

Building upon the literature review, this study proposes the research objective. The aim of this study is to examine passengers behavior during public transport with the consideration of non-stationary and stationary passengers. 

<u>Research question</u>

(RQ1) How do passengers’ attitudes and perceptions influence their movement behavior in crowded-situated public transport, when they are in stationary state and non-stationary state?

(RQ2) What alternative framework can better represent the alighting and boarding process, with the consideration of different passenger type, non-stationary and stationary, incorporated to the examination during crowded-situated in public transport?

<u>Proposed idea</u>

The interactions might be occurred between each passenger type during boarding and alighting process are described as follows:

||Passenger stay inside the car $(PC_{s})$|Passenger stay on the platform waiting for boarding process $(PP_{s})$|Passenger alighting $(PA_{m})$|Passenger boarding $(PB_m)$|
|--|---|------|------|-----|
|**Passenger stay inside the car** $(PC_{s})$|*not decided yet*|na|(5)|(9)|
|**Passenger stay on the platform waiting for boarding process** $(PP_{s})$|na|*not decided yet*|(6)|*similar agent*|
|**Passenger alighting** $(PA_{m})$|(1)|(3)|(2) and (4)|*since DPE there is no interaction*|
|**Passenger boarding** $(PB_m)$|(7)|*similar agent*|*since DPE there is no interaction*|(8)|

Following DPE rule -> First disembarking process/ alighting -> then embarking process/ boarding

Assume within crowding condition

### Alighting process

Passenger alighting $(PA_{m})$

- (1) Collision avoidance with passengers inside the car $(PC_{s})$ since preparing to step out of car
- (2) Leader follower with another passenger alighting.
- (3) Collision avoidance with passenger waiting at the platform preparing for boarding $(PP_{s})$. 
- (4) Collision avoidance with another passenger alighting at the arriving platform.


Passenger stay inside the car $(PC_{s})$
- (5) Collision avoidance with passenger alighting when preparing for stepping out of the car.

Passenger stay on the platform waiting for boarding process $(PP_{s})$

- (6) Collision avoidance with passenger alighting stepping in to arriving platform. 

### Boarding process

Passenger boarding $(PB_{m})$

- (7) Collision avoidance with passenger inside the car $(PC_{s})$ when stepping into the car looking for space for stand.
- (8) Leader-follower interaction within passenger boarding

Passenger stay inside the car $(PC_{s})$

- (9) Collision avoidance since they have to adjust the position when passenger boarding $(PB_{m})$ coming in.



<u>Research gap and contribution</u>
 

|Type of gap|Identified gap|Study approach|Academic contribution|Practical contribution|
|---------|----------|-----------|------------|-------------|
|Empirical gap|Lack of empirical or simulation-based studies on passenger dynamics in public transport that incorporate passenger states (non-stationary and stationary).|Examines passenger dynamics under high-density conditions by incorporating different passenger states.|Provides new evidence on passenger behavior and system performance in crowded scenarios.|By accounting for different passenger states, operators can design more efficient alighting and boarding procedures as well as improved crowd management strategies.|
|Theoretical gap|Existing pedestrian modeling frameworks remain limited in describing pedestrian dynamics in continuous space within a discrete choice framework with taking passenger heterogeneity into account, particularly in high density transit context|Develops a continuous-space pedestrian modeling framework that integrates behavioral decision-making by accounting for passenger heterogeneity.|Establishes a state-aware modeling framework that could represent human interaction during public transport operation||


## Literature Review
Pedestrian dynamics model can be divided by two categories namely continuous model and discrete-based model ([Chen,Xu, et.al, 2017](https://doi.org/10.1080/01441647.2017.1396265)). This study focusses on Below the synthetic literature review of the improvement of the social force model based on previous studies in the past recent years.

|Topics|Proposed|Key feature|Data collection method|Context (location)|References|
|------|--------|------------|--------|:-------:|--------|






## Methodology

### Proposed Data Collection

## Findings/Analysis Result

## Current Challenges and Future Task

### Future Task
`10/05` expand the understanding of individual dynamics within discrete approach proposed by [Robin, Th., et.al.,2009](https://doi.org/10.1016/j.trb.2008.06.010).



