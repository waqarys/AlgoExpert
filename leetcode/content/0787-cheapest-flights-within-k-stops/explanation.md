# 0787. Cheapest Flights Within K Stops

**Difficulty:** Medium | **Category:** Advanced Graphs | **LeetCode:** https://leetcode.com/problems/cheapest-flights-within-k-stops/

## Problem
- Directed flights (from, to, price). Find the cheapest price from src to dst using at most k stops (k + 1 edges), or -1.

## Intuition
- Bellman-Ford limited to k + 1 rounds: after round i, prices[] holds the cheapest cost using at most i edges.
- Each round must relax from a snapshot of the previous round, or a single round could chain several edges.

## Brute Force
- DFS over all paths up to k + 1 edges: exponential.

## Optimal Approach
1. prices = infinity, prices[src] = 0.
2. Repeat k + 1 times: tmp = copy(prices); for each flight (u, v, w) with prices[u] finite: tmp[v] = min(tmp[v], prices[u] + w); prices = tmp.
3. Return prices[dst] or -1.

## Worked Example
- n = 4, flights [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src 0, dst 3, k 1.
```text
round 1 (1 edge):  1=100
round 2 (2 edges): 2=200, 3=700
answer 700 (0->2->3 = 400 would need 2 stops)
```

## Complexity
- Time: O(k * E). Space: O(n).

## Pitfalls
- Relaxing in place without the snapshot gives wrong (too cheap) answers.

## Video Script
- Why plain Dijkstra fails here: the cheapest path may use too many stops.

## Solution
```java file=advancedgraphs/CheapestFlightsWithinKStops.java
package advancedgraphs;

import java.util.*;

/**
 * LC 787 Cheapest Flights Within K Stops.
 * Approach: Bellman-Ford for k+1 rounds, relaxing from a snapshot each round.
 * Time O(k * E), Space O(n).
 */
public class CheapestFlightsWithinKStops {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int[] prices = new int[n];
        Arrays.fill(prices, Integer.MAX_VALUE);
        prices[src] = 0;
        for (int round = 0; round <= k; round++) {
            int[] tmp = prices.clone();
            for (int[] f : flights) {
                if (prices[f[0]] == Integer.MAX_VALUE) continue;
                tmp[f[1]] = Math.min(tmp[f[1]], prices[f[0]] + f[2]);
            }
            prices = tmp;
        }
        return prices[dst] == Integer.MAX_VALUE ? -1 : prices[dst];
    }
}
```

## Tests
```java test=advancedgraphs/CheapestFlightsWithinKStopsTest.java
package advancedgraphs;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CheapestFlightsWithinKStopsTest {
    CheapestFlightsWithinKStops s = new CheapestFlightsWithinKStops();
    @Test void examples() {
        int[][] f = {{0, 1, 100}, {1, 2, 100}, {2, 0, 100}, {1, 3, 600}, {2, 3, 200}};
        assertEquals(700, s.findCheapestPrice(4, f, 0, 3, 1));
        int[][] g = {{0, 1, 100}, {1, 2, 100}, {0, 2, 500}};
        assertEquals(200, s.findCheapestPrice(3, g, 0, 2, 1));
        assertEquals(500, s.findCheapestPrice(3, g, 0, 2, 0));
        assertEquals(-1, s.findCheapestPrice(3, new int[][]{{0, 1, 1}}, 0, 2, 5));
    }
}
```
