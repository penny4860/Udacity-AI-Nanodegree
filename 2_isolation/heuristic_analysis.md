
## Heuristic Analysis

I constructed a heuristic function with the following features.

* number of one's possible moves
* number of one's surrounding empty
	* ![Confusion Matrix](empty.PNG)
	* As shown in the gray color box in the above figure, the number of empty boxes in the surrounding box of the current position is heuristic.
	* The purpose of this heuristic function is to evaluate that the agent is in the center of the board, rather than the edge of the board, in good state.
* number of one's future moves
	* ![Confusion Matrix](future.PNG)
	* The number of possible moves in possible moves, such as the box shown in gray color in the above figure, is heuristically determined.
	* The purpose of this heuristic function is to make the first move of the agent closer to the center.
	

Experimental results show that each feature is effective. For agents that do not use iterative deepning, the odds are close to 100%. However, it failed to consistently win the AB_Improved agent.
