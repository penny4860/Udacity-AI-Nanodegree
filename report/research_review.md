
## Overview

Automated planning and scheduling, sometimes denoted as simply planning, is a branch of artificial intelligence that concerns the realization of strategies or action sequences, typically for execution by intelligent agents, autonomous robots and unmanned vehicles.<sup>1</sup>  Among them, the field of planning is fully observable, deterministic and static is called classical planning.<sup>2</sup> In this paper, I will try to summarize linear planning, partial order planning, and GraphPlan, which play an important role in the history of classical planning.


## 1. linear planning

Early AI planning researchers studied ways to design totally ordered action sequences. This approach, also known as linear planning, used to calculate the subplan for the subgoal and then combine the subplans into a sequence. However, it is known that this method does not guarantee completeness for problem solving. 

## 2. Partial order planning

Partial-order planning is an approach to automated planning that leaves decisions about the ordering of actions as open as possible.<sup>3</sup> It contrasts with linear planning, which produces an exact ordering of actions. Given a problem in which some sequence of actions is required in order to achieve a goal, a partial-order plan specifies all actions that need to be taken, but specifies an ordering of the actions only where necessary. 

Linear planning did not guarantee completeness of the problem, but partial-order planning was found to always find a solution when using breadth-first-search.<sup>4</sup> Partial order planning approach has been the mainstream of planning algorithm for 20 years until 1990s.

 
## 3. GraphPlan

Partial order planning approach has a disadvantage of long computation time, and since the 1990s, faster algorithms have been introduced, guaranteeing completeness like partial order planning. One of them is GraphPlan. GraphPlan construct a graph that encodes constraints on possible plans and use this planning graph to constrain search for a valid plan. The name GraphPlan is due to the use of a novel planning graph, to reduce the amount of search needed to find the solution from straightforward exploration of the state space graph.<sup>5
</sup>

## References

1. https://en.wikipedia.org/wiki/Automated_planning_and_scheduling
2. Russel, Stuart and Norvig, Peter: Künstliche Intelligenz: Ein moderner Ansatz "Artificial Intelligence: A modern approach, 3rd : ch10" (2012)
3. https://en.wikipedia.org/wiki/Partial-order_planning
4. https://courses.cs.washington.edu/courses/cse473/06au/schedule/lect16.pdf
5. https://en.wikipedia.org/wiki/Graphplan
