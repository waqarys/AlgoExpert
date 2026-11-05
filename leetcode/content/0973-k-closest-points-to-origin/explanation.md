# 0973. K Closest Points to Origin

**Difficulty:** Medium | **Category:** Heap / Priority Queue | **LeetCode:** https://leetcode.com/problems/k-closest-points-to-origin/

## Problem
- Return the k points closest to (0,0) by Euclidean distance, in any order.

## Intuition
- Compare squared distances (no sqrt needed).
- Keep a max-heap of size k: if a closer point arrives, evict the farthest of the current k.
- Quickselect gives O(n) average as a follow-up.

## Brute Force
- Sort all points by distance: O(n log n).

## Optimal Approach
1. Max-heap ordered by x*x + y*y.
2. For each point: offer; if size > k, poll.
3. Return the heap contents.

## Worked Example
- points [[3,3],[5,-1],[-2,4]], k = 2.
```text
[3,3] d=18  heap {18}
[5,-1] d=26 heap {26,18}
[-2,4] d=20 heap {26,20,18} -> evict 26
answer [[3,3],[-2,4]]
```

## Complexity
- Time: O(n log k). Space: O(k).

## Pitfalls
- Squared distance can reach 2 * 10^8 for constraints of 10^4 - fits in int, but use long-safe comparisons in general.

## Video Script
- "Top-k smallest -> max-heap of size k" (the mirror image of problem 703).

## Solution
```java file=heap/KClosestPointsToOrigin.java
package heap;

import java.util.*;

/**
 * LC 973 K Closest Points to Origin.
 * Approach: max-heap of size k keyed by squared distance.
 * Time O(n log k), Space O(k).
 */
public class KClosestPointsToOrigin {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Long.compare(dist(b), dist(a)));
        for (int[] p : points) {
            pq.offer(p);
            if (pq.size() > k) pq.poll();
        }
        return pq.toArray(new int[0][]);
    }

    private static long dist(int[] p) { return (long) p[0] * p[0] + (long) p[1] * p[1]; }
}
```

## Tests
```java test=heap/KClosestPointsToOriginTest.java
package heap;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class KClosestPointsToOriginTest {
    static Set<List<Integer>> set(int[][] pts) {
        Set<List<Integer>> s = new HashSet<>();
        for (int[] p : pts) s.add(List.of(p[0], p[1]));
        return s;
    }
    @Test void examples() {
        var s = new KClosestPointsToOrigin();
        assertEquals(Set.of(List.of(-2, 2)), set(s.kClosest(new int[][]{{1, 3}, {-2, 2}}, 1)));
        assertEquals(Set.of(List.of(3, 3), List.of(-2, 4)), set(s.kClosest(new int[][]{{3, 3}, {5, -1}, {-2, 4}}, 2)));
    }
}
```
