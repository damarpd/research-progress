# Public Transit User Dynamics: A Simulation Framework Under Crowding Situation in [location] Context


## Introduction



### General problem and background study

Rapid urbanization has become a defining feature of modern cities globally. To facilitate daily mobility for various trip purposes, such as commuting to work and school, the use of public transportation has been increasingly promoted. This trend has led to a growing demand for public transport systems, particularly metro rail and city bus services, within urban contexts. As passenger demand intensifies, particularly during peak periods, 
maintaining reliable and efficient operations becomes increasingly 
challenging.

Among the various operational processes in public transport, the boarding and alighting process at stops and stations is one of the most critical determinants of service efficiency. This process directly governs dwell time which refers to the duration a vehicle remains stationary at a stop [(Thoreau et al, 2016)](https://onlinelibrary.wiley.com/doi/epdf/10.1002/atr.1446?getft_integrator=sciencedirect_contenthosting&src=getftr&utm_source=sciencedirect_contenthosting), which contributes to cumulative delay across stops. At the network level, [Enayatollahi et al. (2019)](https://link.springer.com/article/10.1007/s12469-019-00203-2) demonstrated that boarding and alighting time is a controllable internal factor directly linked to bus bunching severity, cutting just one second per passenger in boarding and alighting time is sufficient to visibly reduce bunching, even without any other operational change. During off-peak hours, this process proceeds with relative ease. However, under peak-hour conditions, the convergence of high passenger volumes at the platform-vehicle interface creates congestion that disrupts the orderly flow of alighting and boarding.

The significance of this process is well established. [Daamen et al. (2008)](https://doi.org/10.3141/2042-08) noted that dwell time is mostly consumed by the boarding and alighting process itself, identifying it as the primary driver of stop duration. Under crowded conditions, this impact intensifies sharply: [Shen et al. (2026)](https://doi.org/10.1016/j.simpat.2026.103260) demonstrated that once in-carriage density exceeds a critical threshold (LOS D, 2.97 persons/m²), total alighting time more than doubles (+126.3%) and total boarding time more than doubles (+111.8%), with the rate of increase accelerating disproportionately beyond that point.

Critically, the crowded condition introduces a dimension of complexity that extends beyond actively moving passengers alone. Under high occupancy, passengers remaining stationary, whether inside the vehicle or waiting on the platform, are no longer passive elements of the environment. They become active participants whose spatial positioning, yielding decisions, and behavioral responses directly condition the movement of alighting and boarding passengers around them. This interaction between stationary and non-stationary passengers under crowded conditions represents the core operational problem this study addresses, as it remains incompletely characterized in its behavioral dimension.

This is supported by a recent simulation study: [Shen et al. (2026)](https://doi.org/10.1016/j.simpat.2026.103260) showed that including carriage standees and platform-waiting pedestrians as individual agents, rather than ignoring them, is necessary to realistically simulate the boarding and alighting process, since these stationary passengers generate forces that affect how moving passengers navigate around them. Yet their model only accounts for the physical presence of stationary passengers, not their behavior: it cannot capture why a standee chooses to yield, how they reposition, or how their response changes as the crowd around them grows denser.



### Rationale of the study

#### Sub argument 1: Limited consideration of passenger typology in existing studies

Most prior studies have primarily focused on passenger movements associated with entering and exiting vehicles during boarding and alighting processes ([Qu Y., et.al., 2019](https://doi.org/10.1016/j.physa.2019.121075); [Seriani and Fernandez, 2015](https://doi.org/10.1016/j.trc.2015.02.003)). In these studies, only passengers who actively moving included in the analysis process. When crowded situations happen, stationary passengers are also active participants whose spatial adjustments and yielding decisions directly shape the flow around stationary passengers.

Empirical evidence indicates that even within the subset of actively moving passengers, behavioral profiles differ systematically between types. As platform and vehicle occupancy increases during peak hours, passengers experience intensifying time pressure to complete their trip on schedule. Under sufficiently high time pressure, passengers tend to shift from conservative, rule-following behavior toward more competitive behavior, which can escalate into conflicts at the train door ([Qu et al., 2019](https://doi.org/10.1016/j.physa.2019.121075)). Critically, this pressure does not affect all passenger types equally. An asymmetry exists in the consequences of missing the door: a boarding passenger who misses the door merely waits for the next train at the same station, whereas an alighting passenger who misses the door must travel to the next station and return, incurring a substantially higher cost ([Qu et al., 2019](https://doi.org/10.1016/j.physa.2019.121075)). This asymmetry produces systematically distinct behavioral profiles, with alighting passengers exhibit greater urgency, moving faster and more consistently throughout the process, while boarding passengers exhibit comparatively more variable and hesitant movement patterns ([Qu et al., 2019](https://doi.org/10.1016/j.physa.2019.121075)). 

This asymmetric sensitivity to crowding is not unique to metro contexts. In an independent analysis of large-scale smart-card data from Singapore's bus network, [Sun et al. (2014)](https://doi.org/10.1016/j.tra.2014.09.007) found that higher on-board occupancy *increases* boarding time per passenger (+0.340 s/pax) through in-vehicle friction, while simultaneously *decreasing* alighting time per passenger (−0.082 s/pax), as crowding discomfort and social pressure push passengers to exit more quickly. The convergence of this bus-based, data-driven finding with the train-based asymmetry reported by ([Qu et al., 2019](https://doi.org/10.1016/j.physa.2019.121075)) suggests that the differential behavioral response of alighting versus boarding passengers to crowding is a robust phenomenon that generalizes across vehicle types and measurement methods. 

If behavioral distinctness is already observable between alighting and boarding passengers alone, the case for distinguishing passenger types in simulation models becomes empirically unavoidable.

Yet this distinction remains absent from most existing modeling frameworks. Among the few studies that have attempted typological classification, [Li Z. et al. (2020)](https://doi.org/10.1016/j.tra.2019.12.017) made an early attempt at passenger typology by classifying passengers into three types including alighting, boarding, and staying, in their SFM simulation. Staying passengers were given a small degree of reactive capacity: when moving passengers come nearby, they slightly shift their position to yield space. This is a step beyond treating stationary passengers as fixed obstacles. However, the yielding is only a simple physical adjustment, platform-waiting passengers are not included, and no explanation is offered for why a staying passenger yields or how their response changes under crowding.

More recently, [Yining Jia, et.al. (2026)](https://doi.org/10.1016/j.physa.2026.131279) explicitly considers a categorization of metro passengers into three groups comprising boarding, alighting, and remaining on-board passengers. However, their analysis is situated within normal operating conditions, where remaining passengers are typically seated, as supported by controlled experimental settings by [Fu L., et.al., 2023](https://doi.org/10.1016/j.tust.2023.105362). This assumption collapses under crowded real-world conditions, where remaining passengers are predominantly standing, spatially constrained, and compelled to actively respond to the movements of alighting and boarding passengers around them.

[Shen et al. (2026)](https://doi.org/10.1016/j.simpat.2026.103260) takes a step further by using four passenger types in their simulation comprising alighting passengers, boarding passengers, carriage standees, and platform-waiting pedestrians, which matches the full range of passenger states this study also proposes. However, stationary passengers in their model are treated only as physical objects: they are set to have zero speed and simply block or deflect moving passengers through force equations, without any capacity to make decisions or respond to the surrounding situation.

Consequently, even though recent studies have begun to include all four passenger types, stationary passengers are still only represented physically (as an obstacles) rather than as agents who actually decide when to yield, how to move, and how to react as crowding around them increases.

To address this gap, this study proposes four passenger types defined 
by their state during the boarding and alighting process:

| State | Type | Represented by |
|-------|------|----------------|
| Non-stationary | Passenger alighting | $PA_{m}$ |
| | Passenger boarding | $PB_{m}$ |
| Stationary | Passenger staying inside the car | $PC_{s}$ |
| | Passenger staying on the platform waiting to board | $PP_{s}$ |


#### Sub argument 2: Absence of attitudinal and perceptual constructs in existing passenger simulation models

<mark> need a strong anchor at the opening section, given that current study highlighted crowding condition on public transport. Since that crowding considered as subjective perception rather than objective perception, needs to considered perceived crowding in each passenger type to investigate the perceived crowding affecting behavioral responses each passenger type in crowding situation. At this moment the proposed idea of this sub argument 2 would be sub-study of this thesis universe, which has title "Perceived Crowding Impact on Behavioral Response During Public Transport Crowding Considering Passenger Type"</mark>

Behavioral difference across passenger type as evidenced by [Qu et al., (2019)](https://doi.org/10.1016/j.physa.2019.121075), which were represented by the objective measures, such as time (in second), could be the starting point that there is a different underlying motivational state which drives the dynamic behavior of each passenger type. [Stokols (1972)](https://doi.org/10.1037/h0032706) provides the theoretical basis for this: crowding, defined as the psychological experience that arises when a passenger perceives that available space falls below what they need or expect, is fundamentally distinct from density as a physical condition. It is this perceived crowding, not density itself, that generates the motivational state driving how passengers responds. [Kalb and Keating (1981)](https://doi.org/10.1177/014616728174022) confirmed this distinction empirically: feeling crowded and rating the environment as crowded are statistically distinct constructs, with only felt crowding co-loading with confinement and stress, the psychological states most directly relevant to passenger behavior.


Understanding what drives passenger behavior therefore requires shifting the analytical lens from physical parameters to attitudinal and perceptual constructs, specifically, how each passenger type perceives crowding and how that perception shapes their behavioral response. Because $PA_m$, $PB_m$, $PC_s$, and $PP_s$ occupy different positions and face different constraints during the boarding and alighting process, the crowding experience they accumulate, and the behavioral responses it triggers, are not uniform across types and cannot be treated as such.


[Shen et al. (2026)](https://doi.org/10.1016/j.simpat.2026.103260) makes this clear through a deliberate design choice: carriage standees and platform-waiting passengers are intentionally set to zero speed with no ability to react or respond. They are present in the simulation as physical objects — but by design, they do not perceive, decide, or adjust to the situation around them. This is not a flaw in their model; it is a conscious simplification. But it means that how stationary passengers actually behave — where they choose to stand, whether they respond to the alighting flow, and how their reactions change as crowding grows — is intentionally left outside the model's scope, and this is the gap the present study addresses.

This limitation becomes clearer when looking at what the model's own results mean for the passengers involved. [Shen et al. (2026)](https://doi.org/10.1016/j.simpat.2026.103260) found that more alighting passengers produce a shorter exit time — at 2,000 waiting pedestrians, the fastest exit drops from 23.15 s (100 alighting) to 16.40 s (500 alighting) — because a larger alighting group pushes through the waiting crowd more effectively. This looks like a good operational result. But the model only measures time, and only from the alighting side. What it cannot capture is what $PP_s$ (platform-waiting passengers) are experiencing as they are pushed through more intensively. [Mahudin et al. (2012)](https://doi.org/10.1016/j.trf.2011.11.006) showed that feeling crowded is not simply a matter of how many people are present: it is a psychological state that arises when passengers feel their personal space is being exceeded, experienced as feeling confined, disorderly, or chaotic. As alighting volume increases, this feeling is more likely to be triggered in $PP_s$, causing emotional reactions such as feeling hindered, frustrated, and stressed. [Stokols (1972)](https://doi.org/10.1037/h0032706) identified the primary behavioral response to feeling crowded as physically leaving the crowded area to gain more space. Yet $PP_s$ cannot exercise this response, they are committed to boarding at that door and have no option to withdraw. The crowding experience they accumulate during the alighting phase therefore does not disappear; it carries forward and directly conditions how they respond during boarding. This is precisely the contribution this study proposes: to examine how perceived crowding shapes the behavioral response of each passenger types: $PA_m$, $PB_m$, $PC_s$, and $PP_s$, under crowded public transport conditions, a dimension not fully examined by previous studies.




#### Sub argument 3: Existing modeling frameworks are insufficient for representing heterogeneous passenger dynamics in continuous space

In the methodological area of microscopic pedestrian modeling, [Chen, Xu, et.al. (2017)](https://doi.org/10.1080/01441647.2017.1396265) classified pedestrian dynamics models into two primary categories: continuous models and discrete-based models. Each carries specific limitations when applied to the crowded transit boarding and alighting context this study addresses.

Regarding the continuous approach, 
[Seriani and Fernandez (2015)](https://doi.org/10.1016/j.trc.2015.02.003) argued that continuous movement in pedestrian dynamics modeling ensures more realistic spatial representations, as the space is free from artificial restrictions such as cells or grids imposed by Cellular Automata approaches. However, continuous models, while capable of reproducing movement trajectories, do not directly link pedestrian movement to underlying decision-making processes  ([Asano, Iryo and Kuwahara, 2009](https://link.springer.com/chapter/10.1007/978-1-4419-0820-9_28)). This is a critical shortcoming in the crowded boarding and alighting context, where the decision processes of individual passengers — and crucially, of passengers interacting with each other — must be explicitly represented to reproduce realistic flow dynamics under congested conditions.

### Research objective

Building upon the literature review, this study proposes the research objective. The aim of this study is to examine passengers behavior during public transport with the consideration of non-stationary and stationary passengers. 

### Research question

(RQ1) How do passengers’ attitudes and perceptions influence their movement behavior in crowded-situated public transport, when they are in stationary state and non-stationary state?

(RQ2) What alternative framework can better represent the alighting and boarding process, with the consideration of different passenger type, non-stationary and stationary, incorporated to the examination during crowded-situated in public transport?

### Proposed idea

The interactions might be occurred between each passenger type during boarding and alighting process are described as follows:

||Passenger stay inside the car $(PC_{s})$|Passenger stay on the platform waiting for boarding process $(PP_{s})$|Passenger alighting $(PA_{m})$|Passenger boarding $(PB_m)$|
|--|---|------|------|-----|
|**Passenger stay inside the car** $(PC_{s})$|*not decided yet*|na|(5)|(9)|
|**Passenger stay on the platform waiting for boarding process** $(PP_{s})$|na|*not decided yet*|(6)|*similar agent*|
|**Passenger alighting** $(PA_{m})$|(1)|(3)|(2) and (4)|*since DPE there is no interaction*|
|**Passenger boarding** $(PB_m)$|(7)|*similar agent*|*since DPE there is no interaction*|(8)|

Following DPE rule -> First disembarking process/ alighting -> then embarking process/ boarding

Assume within crowding condition

#### Alighting process

Passenger alighting $(PA_{m})$

- (1) Collision avoidance with passengers inside the car $(PC_{s})$ since preparing to step out of car
- (2) Leader follower with another passenger alighting.
- (3) Collision avoidance with passenger waiting at the platform preparing for boarding $(PP_{s})$. 
- (4) Collision avoidance with another passenger alighting at the arriving platform.


Passenger stay inside the car $(PC_{s})$
- (5) Collision avoidance with passenger alighting when preparing for stepping out of the car.

Passenger stay on the platform waiting for boarding process $(PP_{s})$

- (6) Collision avoidance with passenger alighting stepping in to arriving platform. 

#### Boarding process

Passenger boarding $(PB_{m})$

- (7) Collision avoidance with passenger inside the car $(PC_{s})$ when stepping into the car looking for space for stand.
- (8) Leader-follower interaction within passenger boarding

Passenger stay inside the car $(PC_{s})$

- (9) Collision avoidance since they have to adjust the position when passenger boarding $(PB_{m})$ coming in.



### Research gap and contribution
 

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

`21/06` expand understanding another approach by [Hoogendoorn and Bovy 2004](https://doi.org/10.1016/S0191-2615(03)00007-9)



