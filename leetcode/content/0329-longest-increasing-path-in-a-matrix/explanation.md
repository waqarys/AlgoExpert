# 0329. Longest Increasing Path in a Matrix

**Difficulty:** Hard | **Category:** 2-D Dynamic Programming | **LeetCode:** https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

## Problem
- Return the length of the longest strictly increasing path moving up/down/left/right.

## Intuition
- Strictly increasing paths can never revisit a cell, so the "graph" is a DAG and memoisation is safe.
- best(r, c) = 1 + max best(neighbour) over neighbours with a larger value.

## Brute Force
- DFS from every cell without memo: exponential.

## Optimal Approach
1. memo[r][c] = 0 (unknown).
2. dfs(r, c): if memo set, return it; else compute from larger neighbours and store.
3. Answer = max dfs over all cells.

## Worked Example
- [[9,9,4],[6,6,8],[2,1,1]].
```text
path 1 -> 2 -> 6 -> 9 : length 4
memo(9)=1, memo(6)=2, memo(2)=3, memo(1 at (2,1))=4
answer 4
```

## Complexity
- Time: O(m * n). Space: O(m * n).

## Pitfalls
- No visited set needed - strict increase prevents cycles.

## Video Script
- "DFS + memo = DP on a DAG": an important bridge between graphs and DP.

## Solution
```java file=dp2/LongestIncreasingPathInMatrix.java
package dp2;

/**
 * LC 329 Longest Increasing Path in a Matrix.
 * Approach: DFS with memoization over the implicit DAG of increasing moves.
 * Time O(mn), Space O(mn).
 */
public class LongestIncreasingPathInMatrix {
    private static final int[][] DIRS = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int longestIncreasingPath(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length, best = 0;
        int[][] memo = new int[m][n];
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++) best = Math.max(best, dfs(matrix, r, c, memo));
        return best;
    }

    private int dfs(int[][] g, int r, int c, int[][] memo) {
        if (memo[r][c] != 0) return memo[r][c];
        int best = 1;
        for (int[] d : DIRS) {
            int nr = r + d[0], nc = c + d[1];
            if (nr >= 0 && nc >= 0 && nr < g.length && nc < g[0].length && g[nr][nc] > g[r][c])
                best = Math.max(best, 1 + dfs(g, nr, nc, memo));
        }
        return memo[r][c] = best;
    }
}
```

## Tests
```java test=dp2/LongestIncreasingPathInMatrixTest.java
package dp2;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LongestIncreasingPathInMatrixTest {
    LongestIncreasingPathInMatrix s = new LongestIncreasingPathInMatrix();
    @Test void examples() {
        assertEquals(4, s.longestIncreasingPath(new int[][]{{9, 9, 4}, {6, 6, 8}, {2, 1, 1}}));
        assertEquals(4, s.longestIncreasingPath(new int[][]{{3, 4, 5}, {3, 2, 6}, {2, 2, 1}}));
        assertEquals(1, s.longestIncreasingPath(new int[][]{{1}}));
    }
}
```
