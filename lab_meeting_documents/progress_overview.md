# Public Transit User Dynamics Framework: An Adaptive Behavior In Response to Disruptive Event in [Case Study] Context




## Introduction

### Background study

<u>General problem</u>

Rapid urbanization has become a defining feature of modern cities. To facilitate daily mobility for various trip purposes, such as commuting to work and school, the use of public transportation has been increasingly promoted. This trend has led to a growing demand for public transport systems, particularly metro rail and city bus services, within urban contexts. During off-peak hours, operational issues such as delays are relatively uncommon. However, as passenger demand intensifies during peak periods, such issues become more prevalent. In particular, critical processes such as passenger movement/dynamics within boarding and alighting operations can serve as key contributors to these delays.

On the one hand, large-scale events have received considerable scholarly attention due to their potential to disrupt public transport services. In the literature, such phenomena have been conceptualized using various terms, including *mega-events* ([Parkes et.al.,2016](https://doi.org/10.1016/j.tra.2016.07.006)), *disruption/service disruption* ([Pnevmatikou et.al,2015](https://link.springer.com/article/10.1007/s11116-015-9656-4); [Rahimi et.al.,2019](https://doi.org/10.1016/j.trd.2019.10.011)), *shock to the transport system* ([Jenelius E., and Mattsson, L.G.,2021](https://doi.org/10.1016/B978-0-08-102671-7.10719-5)), and *large-scale event* ([Kopsacheilis A., 2026](https://doi.org/10.1080/03081060.2026.2643729)). According to [Parkes et.al.,(2016)](http://dx.doi.org/10.1016/j.tra.2016.07.006), such phenomena are defined as event that draw substantial numbers of individuals to a location, placing the local environment and infrastructure under great pressure, and bringing disruption to residents. Moreover, [Parkes et.al.,(2016)](http://dx.doi.org/10.1016/j.tra.2016.07.006) added that trips generated during the London Olympic Games and Paralympic Games 2012 were geographically specific and contributed significant impact on major underground stations, which reported added significant loadings to the stations that already overcapacity. 

Within the methodological area of microscopics pedestrian modelling, [Chen,Xu, et.al, (2017)](https://doi.org/10.1080/01441647.2017.1396265) classified pedestrian dynamics models into two primary categories namely continuous model and discrete-based model. Among the continuous approaches, the Social Force Model (SFM), originally proposed by [Helbing, D., and Molnar, P.,(1995)](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.51.4282), remains one of the most widely applied frameworks for simulating pedestrian dynamics. SFM has been explored to enhance the understanding of pedestrian dynamics accross various context, including open space such as sidewalks ([Siddhart, S.M.P. and Vedagiri, P., 2018](https://doi.org/10.1177/0361198118758673), [Zhao X., et.al., 2026](https://doi.org/10.3390/su18020746)), emergency situation ([Zhang, et.al.,2023](https://doi.org/10.1080/17538947.2023.2197261)), and metro transit system, speficifically during boarding and alighting process ([Yining Jia, et.al.,2026](https://doi.org/10.1016/j.physa.2026.131279)). 

<u>Rationale of the study</u>

This study expects to introduce novel insights into the field of microscopic pedestrian modeling by situating the proposed framework within the context of public transport operations during large-scale events. Such events are known to generate intense passenger crowding, which can exert direct and substantial pressure on system performance. Despite these conditions, existing modeling approaches have not adequately captured the complexity of passenger interactions under such disrupted and high-density scenarios. 

Most prior studies have primarily focused on passenger movements associated with entering and exiting vehicles during boarding and alighting processes ([Qu Y., et.al.,2019](https://doi.org/10.1016/j.physa.2019.121075), [Seriani and Fernandez, 2015](https://doi.org/10.1016/j.trc.2015.02.003)). In contrast, at this moment, only [Yining Jia, et.al.(2026)](https://doi.org/10.1016/j.physa.2026.131279) explicitly consider a categorization of metro passengers into three groups—boarding, alighting, and remaining on-board passengers. However, their analysis is situated within normal operating conditions, where remaining passengers are typically seated, as supported by controlled experimental settings by [Fu L., et.al., 2023](https://doi.org/10.1016/j.tust.2023.105362). This limits the applicability of existing findings to more complex and crowded real-world contexts

Accordingly, this study places particular emphasis on the dynamics of remaining on-board passengers under crowding conditions induced by large-scale events. In such contexts, these passengers are not passive occupants but actively engage in adaptive behaviors to accommodate boarding and alighting flows. This **adaptive mechanism**, which operates alongside conventional boarding and alighting dynamics, remains insufficiently explored in the literature. Understanding these interactions is critical, as adjustments made by on-board passengers can significantly influence passenger flow efficiency, dwell time, and overall operational performance. Notably, this phenomenon has received limited attention within the Social Force Model (SFM) framework.

In addition, this study seeks to broaden the analytical perspective by incorporating a discrete behavioral modeling approach, introduced by [Robin, Th., et.al.,2009](https://doi.org/10.1016/j.trb.2008.06.010), thereby complementing continuous modeling frameworks and providing a more comprehensive understanding of passenger dynamics under complex and high-density conditions.



<u>Research objective</u>

Building upon the literature review, this study proposes the research objective. The aim of this study is to examine the public transit user adapting behavior under the large-scale event-induced crowding situation.


<u>Research question</u>

(1) How do the adaptive behaviors of passengers influence flow dynamics and operational performance (e.g., dwell time and congestion) during boarding and alighting processes under large-scale event–induced crowding conditions?

(2) *not decided (but related to discrete approach)*



<u>Research gap and contribution</u>
 

|Type of gap|Identified gap|Study approach|Academic contribution|Practical contribution|
|---------|----------|-----------|------------|-------------|
|Empirical gap|Lack of empirical or simulation-based studies on **passenger dynamics** during the large-scale event-induced crowding situated on public transport system|Examines passenger dynamics under high-density conditions|Provides new evidence on passenger behavior and system performance in disrupted scenarios|By understanding how remaining on-board passengers adapt (e.g., repositioning, yielding space), operators can design better boarding/alighting procedures or crowd management during the operations|
|Theoretical gap|The SFM emphasizes individual movement/dynamics by forces but underrepresent on adaptive behavior on remaining passengers during the boarding-alighting process|Introduces adaptation mechanism of on-board passengers within pedestrian dynamics framework|Extends SFM by incorporating adaptivve behavior in high density context|*tbd*|


## Literature Review
Pedestrian dynamics model can be devided by two categories namely continous model and discrete-based model ([Chen,Xu, et.al, 2017](https://doi.org/10.1080/01441647.2017.1396265)). This study focusses on Below the synthetic literature review of the improvement of the social force model based on previous studies in the past recent years.

|Topics|Proposed|Key feature|Data collection method|Context (location)|References|
|------|--------|------------|--------|:-------:|--------|
|Social force model|Original Social Force Model|This framework identify pedestrian motion adopting Newton's second law, which contains three forces determining pedestrian motion||-|[Helbing D., and Molnar P. (1995)](https://doi.org/10.1103/PhysRevE.51.4282)|
|||Three rules are acceleration term (self-driving force), repulsive efect toward other pedestrian and borders, such as building and wall etc, and attractive effect force||||
||Social Force Model Considering Pedestrian Characteristics and Behavior (SFMPCB)|Incorporating social characteristic of pedestrian specifically gender||Sidewalk (in Mumbai, India)|[Siddhart, S.M.P. and Vedagiri, P., (2018)](https://doi.org/10.1177/0361198118758673)|
|||Gender characteristic is represented as reaction time $\tau_{m/f}$||||
|||Conducted in normal pedestrian behavior||||
||Improved Social Force Model (ISFM)|Simulating pedestrian motion (evacuation) during subway station fire incident||Subway station|[Zhang, et.al.,2023](https://doi.org/10.1080/17538947.2023.2197261)|
|||Proposed model which take 'environmental role' $(f_{ie})$ and a 'subjective initiative' $(f_{ig})$ into account||||
||Modified Social Force Model (MSFM)|This proposed-model explored passenger dynamics during **boarding and alighting in metro transit system**||Metro transit system|[Yining Jia, et.al.,2026](https://doi.org/10.1016/j.physa.2026.131279)|
|||MSFM considered eliptical agents, rotational dynamics, and specific DPE (Disembarking Preceed Embarking) rule.|||
|||A new attraction force is proposed to MSFM $(f_{ig})$ to define behavior of following other pedestrians and avoiding obstacles|||
||Enhanced Social Force Model|This study developed a simulation methodology that better reflects real pedestrian behavior particularly on group coordination and avoidance behaviors, including three proposed features for improving original model||Pedestrian path at commercial street in Nanchang City|[Zhao X., et.al., 2026](https://doi.org/10.3390/su18020746)|
|||**Pedestrian effective binocular vision range** is limited at 120 $^o$, meaning that pedestrians can only perceive others within 120 $^o$ sector centered on their walking direction||||
|||Improvement made by incorporating **group-type categorization** -> improved pairing behavior model-> this study proposed heterogenous form of group pedestrian into the model by varying pedestrian social relationship denoted as $T_g$; $T_{g} \in (T_{gfd}, T_{gcl}, T_{gfy}, T_{ged})$||||
|||**Evasion maneuveurs**-> collective avoidance forces meaning that a group of pedestrian preceed avoidance maneuver collectively comprising (a) unified avoidance and (b) inter-weavering avoidance -> this study proposed as accompanying pedestrian avoidance force $(f_{gr})$||||

Below related to large-event scale type:
|Large-scale event type|Event year|Host country/city|Key features|References|
|----------------------|:--------:|:---------------:|------------|----------|
|FIFA World cup|2022|Qatar|this study examining the impact of the FIFA World Cup 2022 and evaluating the effectiveness of various TDM measures on traveler behavior across different sociodemographic segments|[Mohammed, A., et.al. (2025)](https://doi.org/10.1016/j.cstp.2025.101469)|




## Methodology

### Proposed Data Collection

## Findings/Analysis Result

## Current Challenges and Future Task

### Future Task
`10/05` expand the understanding of individual dynamics within discrete approach proposed by [Robin, Th., et.al.,2009](https://doi.org/10.1016/j.trb.2008.06.010).



