# individual notes
This file is created as compilation of notes derived from each `weekly progress` file as indicated the filename format `yyyy-mm-dd.md` in the `progress` folder. Additionally, this file also highlighted the future task should be undertaken to make progress on the research.

## 2026-04-03.md file
### Notes for new terms:
- Critically evaluated
- Pedestrian's self organization behavior
- Reactive responses

### Notes for additional content to research proposal:
- Examined passenger adaptive behavior responses, in this study, defined as movement behavior/dynamics, by using pedestrian dynamics models (e.g., social force model, pedestrian's self organization behavior) 
- This study will consider unique environment (i.e., in the public transportation vehicle characterized not open space and typically occured with high passenger density).
- Also incorporating empirical phenomena such as disruptive services within public transportation system.
- Pedestrian dynamics model can be devided by two categories namely continous model and discrete-based model ([Chen,Xu, et.al, 2017](https://doi.org/10.1080/01441647.2017.1396265))


## 2026-04-11.md file
### Notes for new terms:
- pedestrian microscopic simulation model
- considering missing pedestrian attributes
- oscillatory flow
- crowd control -> usually organized in large-scale event (i.e. music concert)

### Notes for additional content to research proposal:
- Upon the 11/04 progress literature review, this study proposes research questions as a basis to develop research objectives.
- A proposed research questions (tbc to sensei) can be indicated as follow
> (1) How do passengers adapt (related to motion,dynamics, and group form) in response to disruptive events occur in public transportation services? (2) How do transit agency supposed to organize the crowd during the disruptive events?
- A proposed general research objective (tbc to sensei) can be addressed as follow:
> (1) To understand passengers dynamics as a result adaptive response behavior to disruptive events in public transport services; (2) To develop crowd control framework in public transportation system during disruptive event.


## 27/04
- Research title idea -> Public Transit User Dynamics Prediction/Simulation Framework: An Adaptive Behavior Response to Disruptive Event in Japan Context

## 09/05 -10/05
- academic contribution and practical contribution
- structure the background study
- define the research gap
- define the empirical issue occured in public transportation operations currently both during regular working day (peak and non-peak hour) and large scale event -> provide the findings
- Below a proposed structure to `background study`, `research question`

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

Building upon the literature review, this study proposes the research objective. The aim of this study is to examine the public transit user adapting behavior under the large-scale event-induced crowding situated



<u>Research question</u>

(1) How do the adaptive behaviors of passengers influence flow dynamics and operational performance (e.g., dwell time and congestion) during boarding and alighting processes under large-scale event–induced crowding conditions?

(2) *not decided (but related to discrete approach)*



<u>Research gap and contribution</u>
 

|Type of gap|Identified gap|Study approach|Academic contribution|Practical contribution|
|---------|----------|-----------|------------|-------------|
|Empirical gap|Lack of empirical or simulation-based studies on **passenger dynamics** during the large-scale event-induced crowding situated on public transport system|Examines passenger dynamics under high-density conditions|Provides new evidence on passenger behavior and system performance in disrupted scenarios|By understanding how remaining on-board passengers adapt (e.g., repositioning, yielding space), operators can design better boarding/alighting procedures or crowd management during the operations|
|Theoretical gap|The SFM emphasizes individual movement/dynamics by forces but underrepresent on adaptive behavior on remaining passengers during the boarding-alighting process|Introduces adaptation mechanism of on-board passengers within pedestrian dynamics framework|Extends SFM by incorporating adaptivve behavior in high density context|*tbd*|

### Future task
List to expand understanding
|Authors|Key finding|
|---|---|
|[Seriani and Fernandez, (2015)](https://doi.org/10.1016/j.trc.2015.02.003)|**Title:** Pedestrian traffic management of boarding and alighting in metro stations, **Key finding:** **Note from literature:** However, as the passenger demand increases, the dwell time becomes more dependent on boarding and alighting operations and “station dwell times are the major component of headways at short frequencies” (TRB, 2003: 5–19). The authors also argued that continous movement on pedestrian dynamics modelling ensure more realistic representations as the space is free from artificial restrictions, such as celss or grids in Cellular Automata approach|



## 31/05

### Developing alternative framework incorporating passengers interactions between passenger type during boarding and alighting process  

- This study focuses on the public transport operation, specifically during boarding and alighting process.
- In a crowd, the behavior of each pedestrian is different, since it severely influences the movement characteristics, thus, developing crowd model by implementing multiple pedestrian classes is essential ([Duives D.C.,Daamen W., Hoogendoorn S.P., 2013](https://doi.org/10.1016/j.trc.2013.02.005)).
- Adopting from [Fujiwara, K., et al. (n.d.)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5163637) study, the key players/agents carrying out the process are introduced/proposed in my study (note this is assumed in crowding situation happened inside the car/vehicle in terms of public transport system):

|||Staying|Staying|
|--|---|------|------|
||**State**|Passenger stay inside the car $(PC_{s})$|Passenger stay on the platform waiting for boarding process $(PP_{s})$|
|**Moving**|Passenger alighting $(PA_{m})$|Interaction = $PC_{s}$ might adjust the position to allow $PA_{m}$ prepare for alighting|Interaction = $PA_{m}$ moves on to the platform while avoiding $PP_{s}$ standing on the platform, $PP_{s}$ might adjust the location |
|**Moving**|Passenger boarding $(PB_m)$|Interaction = $PB_{m}$ moves into trains looking for space to stand, $PC_{s}$ might adjust the position giving space for $PB_{m}$| *not sure yet*

- Below detailed description of each interaction possibly occurred between each passenger type -> *need to be discussed*

<u>*PAm* and *PPs* Interaction</u>

- Interaction between $PA_{m}$ and $PP_{s}$ might be occurred during the boarding-alighting process, according to [Shen et al (2026)](https://doi.org/10.1016/j.simpat.2026.103260) incorporates this into the simulation which situated when the walking process from the train door to the vertical pedestrian transit facility (e.g. stair or elevator), the movement of an alighting passenger is affected by the waiting passengers on the platform.
- Considered in collision avoidance behavioral aspect.

<u>*PAm* and *PCs* Interactions</u>
- Considered in collision avoidance behavioral aspect.


<u>*PBm* and *PCs* Interaction</u>
- Considered in collision avoidance behavioral aspect.


### Assessing passengers dynamics through microscopic and macroscopic lens 

- [Qu et al (2019)](https://doi.org/10.1016/j.physa.2019.121075) assessed pedestrian dynamics through video-recorded data, generating pedestrian metrics, from microscopic and macroscopic lens

|Category|Description|Estimated Output|
|----|----------|------|
|Microscopic|Individual movement data and the interactions between consecutive passengers|Time headway distribution|
|||Behavioral patterns|
|||Individual movement characteristics|
|Macroscopic|This analysis evaluates the aggregate behavior and overall performance of the crowd flow|Inflow and outflow rates|
|||Bottleneck capacity utilization|
|||Dwell time estimation|

### Examining passengers attitudes toward crowding on public transport

- Possibility to examination of passengers attitude towards crowding on the public transport station considering proposed passengers' type.

