# 0417. Pacific Atlantic Water Flow

**Difficulty:** Medium | **Category:** Graphs | **LeetCode:** https://leetcode.com/problems/pacific-atlantic-water-flow/

## Problem
- Water flows to a neighbour with height <= current. The Pacific touches the top and left edges, the Atlantic the bottom and right. Return cells that can reach both oceans.

## Intuition
- Searching from every cell is expensive. Reverse the flow: start from each ocean's border and climb to neighbours with height >= current.
- Cells reached by both reverse searches are the answer.

## Brute Force
- DFS from every cell to see whether it reaches each ocean: O((mn)^2).

## Optimal Approach
1. pac/atl boolean grids.
2. DFS from all top/left cells into pac; from all bottom/right cells into atl, moving only uphill (>=).
3. Collect cells with pac && atl.

## Worked Example
- 5x5 example from LeetCode.
```text
Pacific reverse-DFS starts on row 0 and column 0
Atlantic reverse-DFS starts on row 4 and column 4
intersection: [0,4] [1,3] [1,4] [2,2] [3,0] [3,1] [4,0]
```

## Complexity
- Time: O(m * n). Space: O(m * n).

## Pitfalls
- The comparison is reversed (>=) because we walk against the water.

## Video Script
- "Think backwards": multi-source search from the destination.

## Solution
```java file=graphs/PacificAtlanticWaterFlow.java
package graphs;

import java.util.*;

/**
 * LC 417 Pacific Atlantic Water Flow.
 * Approach: reverse DFS uphill from each ocean's border; answer = cells reached by both.
 * Time O(mn), Space O(mn).
 */
public class PacificAtlanticWaterFlow {
    public List<List<Integer>> pacificAtlantic(int[][] h) {
        int m = h.length, n = h[0].length;
        boolean[][] pac = new boolean[m][n], atl = new boolean[m][n];
        for (int r = 0; r < m; r++) { dfs(h, r, 0, pac, h[r][0]); dfs(h, r, n - 1, atl, h[r][n - 1]); }
        for (int c = 0; c < n; c++) { dfs(h, 0, c, pac, h[0][c]); dfs(h, m - 1, c, atl, h[m - 1][c]); }
        List<List<Integer>> res = new ArrayList<>();
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++) if (pac[r][c] && atl[r][c]) res.add(List.of(r, c));
        return res;
    }

    private void dfs(int[][] h, int r, int c, boolean[][] seen, int prev) {
        if (r < 0 || c < 0 || r >= h.length || c >= h[0].length || seen[r][c] || h[r][c] < prev) return;
        seen[r][c] = true;
        dfs(h, r + 1, c, seen, h[r][c]); dfs(h, r - 1, c, seen, h[r][c]);
        dfs(h, r, c + 1, seen, h[r][c]); dfs(h, r, c - 1, seen, h[r][c]);
    }
}
```

## Tests
```java test=graphs/PacificAtlanticWaterFlowTest.java
package graphs;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class PacificAtlanticWaterFlowTest {
    @Test void examples() {
        int[][] h = {{1, 2, 2, 3, 5}, {3, 2, 3, 4, 4}, {2, 4, 5, 3, 1}, {6, 7, 1, 4, 5}, {5, 1, 1, 2, 4}};
        assertEquals(List.of(List.of(0, 4), List.of(1, 3), List.of(1, 4), List.of(2, 2), List.of(3, 0), List.of(3, 1), List.of(4, 0)),
                new PacificAtlanticWaterFlow().pacificAtlantic(h));
        assertEquals(List.of(List.of(0, 0)), new PacificAtlanticWaterFlow().pacificAtlantic(new int[][]{{1}}));
    }
}
```
