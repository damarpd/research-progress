# Public Transit User Dynamics Prediction/Simulation Framework: An Adaptive Behavior Response to Disruptive Event in [Case Study] Context




## Introduction

### Background study

<u>General problem</u>

Rapid urbanization has become a defining feature of modern cities. To facilitate daily mobility for various trip purposes, such as commuting to work and school, the use of public transportation has been increasingly promoted. This trend has led to a growing demand for public transport systems, particularly metro rail and city bus services, within urban contexts. During off-peak hours, operational issues such as delays are relatively uncommon. However, as passenger demand intensifies during peak periods, such issues become more prevalent. In particular, critical processes such as passenger movement/dynamics within boarding and alighting operations can serve as key contributors to these delays.

On the one hand, large-scale events have received considerable scholarly attention due to their potential to disrupt public transport services. In the literature, such phenomena have been conceptualized using various terms, including *mega-events* ([Parkes et.al.,2016](https://doi.org/10.1016/j.tra.2016.07.006)), *disruption/service disruption* ([Pnevmatikou et.al,2015](https://link.springer.com/article/10.1007/s11116-015-9656-4); [Rahimi et.al.,2019](https://doi.org/10.1016/j.trd.2019.10.011)), *shock to the transport system* ([Jenelius E., and Mattsson, L.G.,2021](https://doi.org/10.1016/B978-0-08-102671-7.10719-5)), and *large-scale event* ([Kopsacheilis A., 2026](https://doi.org/10.1080/03081060.2026.2643729)). According to [Parkes et.al.,(2016)](http://dx.doi.org/10.1016/j.tra.2016.07.006), such phenomena are defined as event that draw substantial numbers of individuals to a location, placing the local environment and infrastructure under great pressure, and bringing disruption to residents. 

Within the methodological area of microscopics pedestrian modelling, [Chen,Xu, et.al, (2017)](https://doi.org/10.1080/01441647.2017.1396265) classified pedestrian dynamics models into two primary categories namely continuous model and discrete-based model. Among the continuous approaches, the Social Force Model (SFM), originally proposed by [Helbing, D., and Molnar, P.,(1995)](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.51.4282), remains one of the most widely applied frameworks for simulating pedestrian dynamics. SFM has been explored to enhance the understanding of pedestrian dynamics accross various context, including open space such as sidewalks ([Siddhart, S.M.P. and Vedagiri, P., 2018](https://doi.org/10.1177/0361198118758673), [Zhao X., et.al., 2026](https://doi.org/10.3390/su18020746)), emergency situation ([Zhang, et.al.,2023](https://doi.org/10.1080/17538947.2023.2197261)), and metro transit system, speficifically during boarding and alighting ([Yining Jia, et.al.,2026](https://doi.org/10.1016/j.physa.2026.131279)). 

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
|Large-scale event||||||
|Crowding (related to public transport)|||||


## Methodology

### Proposed Data Collection

## Findings/Analysis Result

## Current Challenges and Future Plan



