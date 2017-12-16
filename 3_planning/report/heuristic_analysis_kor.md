

## 1. Optimal plan for each problems

Breadth First Search (BFS) 는 tree 의 leaf node 중에서 shortest node 를 우선적으로 search 하기 때문에 planning 문제에서의 optimal solution 을 보장한다. 따라서 각 problem 에서의 optimal solution 은 BFS 에서 찾은 plan 으로 구할 수 있다.

```
* P1
	Load(C1, P1, SFO) -> Load(C2, P2, JFK) -> Fly(P2, JFK, SFO) -> Unload(C2, P2, SFO) -> Fly(P1, SFO, JFK) -> Unload(C1, P1, JFK)

* P2
	Load(C1, P1, SFO) -> Load(C2, P2, JFK) -> Load(C3, P3, ATL) -> Fly(P2, JFK, SFO) -> Unload(C2, P2, SFO) -> Fly(P1, SFO, JFK) -> Unload(C1, P1, JFK) -> Fly(P3, ATL, SFO) -> Unload(C3, P3, SFO)

* P3
	Load(C1, P1, SFO) -> Fly(P1, SFO, ATL) -> Load(C3, P1, ATL) -> Fly(P1, ATL, JFK) -> Load(C2, P1, JFK) -> Unload(C1, P1, JFK) -> Unload(C3, P1, JFK) -> Fly(P1, JFK, ORD) -> Load(C4, P1, ORD) -> Fly(P1, ORD, SFO) -> Unload(C2, P1, SFO) -> Unload(C4, P1, SFO)
```

## 2. non-heuristic search 

non-heuristic search 는 additional information 없이 goal state 까지의 path 를 search 한다. 아래의 표는 세가지 non-heuristic search 에 대한 실험결과를 보여준다.

![Confusion Matrix](non-heuristic.PNG)

* BFS 는 모든 문제에서 optimal plan 을 찾았다. non-heuristic search 로 optimal solution 을 찾아야 하는 문제에서는 BFS 를 우선적으로 고려하는 것이 바람직하다.
* Depth First Search (DFS) 는 모든 문제에서 optimal plan 을 찾지 못했다. 그러나 DFS 는 deepest node 를 먼저 expand 하기 때문에 storage cost 측면에서 장점이 있다. 또한 BFS 에 비해서 연산시간이 매우 적게 걸렸다. 구지 optimal solution 을 찾을 필요가 없고, system resource 가 제한적인 환경에서는 BFS 를 사용하는 것 보다 DFS 를 사용하는 것이 더 좋은 방법일 수 있을 것이다. 
* Uniform Cost Search (UFS) 도 BFS 와 마찬가지로 모든 문제에서 optimal plan 을 찾았다. path cost 가 동일하지 않은 문제에서는 BFS 대신 UFS 를 사용하는 것이 더 좋은 방법일 것이다. path cost 가 동일한 문제에서 UFS 는 BFS 와 거의 비슷한 방식으로 search 한다. 하지만, BFS 는 solution 을 찾고 바로 search 를 끝내기 때문에 이 경우에는 BFS 가 UFS 보다 더 좋은 방법이다.

## 3. Heuristic search 

Heuristic search 는 problem 에 대한 knowledge 를 이용해서 search 를 효율적으로 수행하는 방법이다. 아래의 표는 두 가지 heuristic search 에 대한 실험결과이다.

![Confusion Matrix](heuristic.PNG)

* Ignore preconditions heuristic 은 action 에 대한 모든 precondition 을 무시함으로써 문제를 쉽게 만들고, goal state 에 도달하기 위한 minimum number of step 을 count 한다. (AIMA 10.2.3) Ignore preconditions heuristic 을 사용한 A\*-search 는 모든 문제에서 optimal solution 을 찾았다. BFS 에 비해 항상 optimal solution 을 보장한다는 점은 같지만, 문제가 더 복잡해 질 수록 time and space complexity 에서 더 좋은 성능을 보였다. BFS 는  tree 의 depth 에 space and time complexity 가 exponential 하게 증가한다. (AIMA 3.4.1) 따라서 Initial State 에서 Goal State 까지의 step 이 큰 문제에서는  Ignore preconditions heuristic 을 사용한 A\*-search 가 BFS 보다 더 좋은 선택이다.
* Level sum heuristic 을 사용한 A\*-search 는 모든 문제에서 optimal solution 을 찾았다. 이 strategy 는 storage cost 측면에서 강점을 보였다. BFS 는 물론, Ignore preconditions heuristic 을 사용한 A\*-search 보다도 expansion node 수가 매우 적었다. 반면에 time complexity 측면에서는 매우 나쁜 성능을 보였다. 3개의 모든 문제에서 BFS 보다 search time 이 더 오래걸렸다. Level sum heuristic 을 사용한 A\*-search 는 space complexity 가 매우 제한적인 환경에서 항상 optimal solution 을 찾아야 할 때 사용할 수 있는 좋은 방법이 될 것이다.


## 4. Best Heuristics in the problem

Best Heuristic 은 time complexity 와 space complexity 중에서 어떤 성능을 우선시 하느냐에 따라서 다르지만 두 가지 요소를 종합적으로 고려한다면 ignore preconditions heuristic 이 level sum heuristic 보다 더 좋은 heuristic 이라고 할 수 있다.

먼저, time complexity 측면에서는 ignore preconditions heuristic 이 level sum heuristic 보다 더 좋은 성능을 보였고, optimal solution 을 보장하는 non-heuristic search 와 비교해서는 time complexity 와 space complexity 모두 더 좋은 성능을 보였다. 따라서 A\*-search with ignore preconditions heuristic 은 non-heuristic search 보다 항상 좋은 성능을 보장한다고 말할 수 있다.

space complexity 측면에서는  level sum heuristic 이 ignore preconditions heuristic 보다 더 좋은 성능을 보였다. 그러나, level sum heuristic 을 사용한 A\*-search 는 time complexity 측면에서 non-heuristic search 보다도 안 좋은 성능을 보였다. 






