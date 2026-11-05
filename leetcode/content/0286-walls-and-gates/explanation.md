# 0286. Walls and Gates

**Difficulty:** Medium | **Category:** Graphs | **LeetCode:** https://leetcode.com/problems/walls-and-gates/

## Problem
- Grid: -1 wall, 0 gate, INF (2147483647) empty room. Fill each room with the distance to its nearest gate; unreachable rooms stay INF.

## Intuition
- Multi-source BFS from all gates simultaneously: the first time BFS reaches a room is via its nearest gate.

## Brute Force
- BFS from each room to find the nearest gate: O((mn)^2).

## Optimal Approach
1. Enqueue all gates.
2. Pop a cell; for each neighbour that is INF, set it to cell + 1 and enqueue.

## Worked Example
```text
INF  -1  0  INF          3 -1 0 1
INF INF INF  -1    ->    2  2 1 -1
INF  -1 INF  -1          1 -1 2 -1
  0  -1 INF INF          0 -1 3 4
```

## Complexity
- Time: O(m * n). Space: O(m * n).

## Pitfalls
- Only expand into INF cells; that check doubles as the visited test.

## Video Script
- Same skeleton as Rotting Oranges, but we record distances rather than minutes.

## Solution
```java file=graphs/WallsAndGates.java
package graphs;

import java.util.*;

/**
 * LC 286 Walls and Gates.
 * Approach: multi-source BFS from every gate; first visit gives the nearest distance.
 * Time O(mn), Space O(mn).
 */
public class WallsAndGates {
    static final int INF = Integer.MAX_VALUE;

    public void wallsAndGates(int[][] rooms) {
        int m = rooms.length, n = rooms[0].length;
        Deque<int[]> q = new ArrayDeque<>();
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++) if (rooms[r][c] == 0) q.add(new int[]{r, c});
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            for (int[] d : dirs) {
                int r = cur[0] + d[0], c = cur[1] + d[1];
                if (r < 0 || c < 0 || r >= m || c >= n || rooms[r][c] != INF) continue;
                rooms[r][c] = rooms[cur[0]][cur[1]] + 1;
                q.add(new int[]{r, c});
            }
        }
    }
}
```

## Tests
```java test=graphs/WallsAndGatesTest.java
package graphs;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class WallsAndGatesTest {
    static final int I = Integer.MAX_VALUE;
    @Test void example() {
        int[][] g = {{I, -1, 0, I}, {I, I, I, -1}, {I, -1, I, -1}, {0, -1, I, I}};
        new WallsAndGates().wallsAndGates(g);
        assertArrayEquals(new int[][]{{3, -1, 0, 1}, {2, 2, 1, -1}, {1, -1, 2, -1}, {0, -1, 3, 4}}, g);
        int[][] g2 = {{I, -1}, {-1, 0}};
        new WallsAndGates().wallsAndGates(g2);
        assertArrayEquals(new int[][]{{I, -1}, {-1, 0}}, g2);
    }
}
```
