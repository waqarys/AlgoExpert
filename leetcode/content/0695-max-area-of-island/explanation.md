# 0695. Max Area of Island

**Difficulty:** Medium | **Category:** Graphs | **LeetCode:** https://leetcode.com/problems/max-area-of-island/

## Problem
- Grid of 0/1. Return the largest island area (number of cells), or 0.

## Intuition
- Number of Islands, but the flood fill returns how many cells it sank.

## Brute Force
- BFS per island with a visited matrix: same complexity.

## Optimal Approach
1. area(r, c): out of bounds or 0 -> 0; else set 0 and return 1 + area of 4 neighbours.
2. Answer = max over all cells.

## Worked Example
```text
0 1 1
1 1 0     cells (0,1),(0,2),(1,0),(1,1) connected -> area 4
0 0 1     cell (2,2) alone -> area 1
answer 4
```

## Complexity
- Time: O(m * n). Space: O(m * n) recursion worst case.

## Pitfalls
- Mark before recursing so a cell is not counted twice.

## Video Script
- One-line change from problem 200: make DFS return a value.

## Solution
```java file=graphs/MaxAreaOfIsland.java
package graphs;

/**
 * LC 695 Max Area of Island.
 * Approach: DFS flood fill returning the number of cells sunk.
 * Time O(mn), Space O(mn).
 */
public class MaxAreaOfIsland {
    public int maxAreaOfIsland(int[][] grid) {
        int best = 0;
        for (int r = 0; r < grid.length; r++)
            for (int c = 0; c < grid[0].length; c++) best = Math.max(best, area(grid, r, c));
        return best;
    }

    private int area(int[][] g, int r, int c) {
        if (r < 0 || c < 0 || r >= g.length || c >= g[0].length || g[r][c] == 0) return 0;
        g[r][c] = 0;
        return 1 + area(g, r + 1, c) + area(g, r - 1, c) + area(g, r, c + 1) + area(g, r, c - 1);
    }
}
```

## Tests
```java test=graphs/MaxAreaOfIslandTest.java
package graphs;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MaxAreaOfIslandTest {
    MaxAreaOfIsland s = new MaxAreaOfIsland();
    @Test void examples() {
        assertEquals(4, s.maxAreaOfIsland(new int[][]{{0, 1, 1}, {1, 1, 0}, {0, 0, 1}}));
        assertEquals(0, s.maxAreaOfIsland(new int[][]{{0, 0, 0, 0}}));
        assertEquals(6, s.maxAreaOfIsland(new int[][]{
                {0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
                {0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0},
                {0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0}}));
    }
}
```
