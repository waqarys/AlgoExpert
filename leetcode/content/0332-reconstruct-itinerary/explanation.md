# 0332. Reconstruct Itinerary

**Difficulty:** Hard | **Category:** Advanced Graphs | **LeetCode:** https://leetcode.com/problems/reconstruct-itinerary/

## Problem
- Given airline tickets [from, to], build the itinerary starting at "JFK" that uses every ticket exactly once. If several exist, return the lexicographically smallest.

## Intuition
- Using every edge exactly once is an Eulerian path.
- Hierholzer's algorithm: DFS greedily taking the smallest destination; when a node has no unused edges left, prepend it to the route. Dead ends are naturally pushed to the end.

## Brute Force
- Backtracking over sorted destinations, undoing on dead ends: correct but exponential in the worst case.

## Optimal Approach
1. Map airport -> min-heap of destinations.
2. dfs(a): while heap(a) non-empty, dfs(heap.poll()). Then addFirst(a).
3. Result is the route list.

## Worked Example
- [[JFK,KUL],[JFK,NRT],[NRT,JFK]].
```text
dfs JFK -> KUL (smallest) : KUL has no edges -> route [KUL]
back at JFK -> NRT -> JFK : JFK empty now -> route [JFK,KUL]
NRT done -> [NRT,JFK,KUL] ; JFK done -> [JFK,NRT,JFK,KUL]
```

## Complexity
- Time: O(E log E). Space: O(E).

## Pitfalls
- Greedy "smallest first" without post-order insertion fails on the KUL dead-end example.

## Video Script
- Introduce Eulerian paths with the Königsberg bridges story.

## Solution
```java file=advancedgraphs/ReconstructItinerary.java
package advancedgraphs;

import java.util.*;

/**
 * LC 332 Reconstruct Itinerary.
 * Approach: Hierholzer's algorithm with min-heaps for lexical order; post-order prepend.
 * Time O(E log E), Space O(E).
 */
public class ReconstructItinerary {
    private final Map<String, PriorityQueue<String>> g = new HashMap<>();
    private final LinkedList<String> route = new LinkedList<>();

    public List<String> findItinerary(List<List<String>> tickets) {
        for (List<String> t : tickets) g.computeIfAbsent(t.get(0), k -> new PriorityQueue<>()).add(t.get(1));
        dfs("JFK");
        return route;
    }

    private void dfs(String a) {
        PriorityQueue<String> pq = g.get(a);
        while (pq != null && !pq.isEmpty()) dfs(pq.poll());
        route.addFirst(a);
    }
}
```

## Tests
```java test=advancedgraphs/ReconstructItineraryTest.java
package advancedgraphs;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class ReconstructItineraryTest {
    @Test void examples() {
        assertEquals(List.of("JFK", "MUC", "LHR", "SFO", "SJC"), new ReconstructItinerary().findItinerary(List.of(
                List.of("MUC", "LHR"), List.of("JFK", "MUC"), List.of("SFO", "SJC"), List.of("LHR", "SFO"))));
        assertEquals(List.of("JFK", "ATL", "JFK", "SFO", "ATL", "SFO"), new ReconstructItinerary().findItinerary(List.of(
                List.of("JFK", "SFO"), List.of("JFK", "ATL"), List.of("SFO", "ATL"), List.of("ATL", "JFK"), List.of("ATL", "SFO"))));
        assertEquals(List.of("JFK", "NRT", "JFK", "KUL"), new ReconstructItinerary().findItinerary(List.of(
                List.of("JFK", "KUL"), List.of("JFK", "NRT"), List.of("NRT", "JFK"))));
    }
}
```
