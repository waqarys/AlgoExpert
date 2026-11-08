# 0130. Surrounded Regions

**Difficulty:** Medium | **Category:** Graphs | **LeetCode:** https://leetcode.com/problems/surrounded-regions/

## Problem
- Flip every 'O' region that is fully surrounded by 'X' into 'X'. Regions touching the border survive.

## Intuition
- It is easier to find the survivors: flood-fill from every border 'O' and mark it safe ('S').
- Then every remaining 'O' is captured (-> 'X') and every 'S' is restored to 'O'.

## Brute Force
- For each region check whether it touches the border, with a BFS per region: same order but more bookkeeping.

## Optimal Approach
1. DFS from each border 'O', marking 'S'.
2. Sweep: 'O' -> 'X', 'S' -> 'O'.

## Worked Example
```text
X X X X        X X X X
X O O X   ->   X X X X     inner region captured
X X O X        X X X X
X O X X        X O X X     border-connected O survives
```

## Complexity
- Time: O(m * n). Space: O(m * n) recursion worst case.

## Pitfalls
- Do not flip during the first pass; mark first, flip later.

## Video Script
- Pairs well with 417: "start from the border" trick.

## Solution
```java file=graphs/SurroundedRegions.java
package graphs;

/**
 * LC 130 Surrounded Regions.
 * Approach: mark border-connected 'O' as safe via DFS, then capture the rest.
 * Time O(mn), Space O(mn).
 */
public class SurroundedRegions {
    public void solve(char[][] b) {
        int m = b.length, n = b[0].length;
        for (int r = 0; r < m; r++) { mark(b, r, 0); mark(b, r, n - 1); }
        for (int c = 0; c < n; c++) { mark(b, 0, c); mark(b, m - 1, c); }
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++) b[r][c] = b[r][c] == 'S' ? 'O' : 'X';
    }

    private void mark(char[][] b, int r, int c) {
        if (r < 0 || c < 0 || r >= b.length || c >= b[0].length || b[r][c] != 'O') return;
        b[r][c] = 'S';
        mark(b, r + 1, c); mark(b, r - 1, c); mark(b, r, c + 1); mark(b, r, c - 1);
    }
}
```

## Tests
```java test=graphs/SurroundedRegionsTest.java
package graphs;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SurroundedRegionsTest {
    static char[][] g(String... rows) {
        char[][] b = new char[rows.length][];
        for (int i = 0; i < rows.length; i++) b[i] = rows[i].toCharArray();
        return b;
    }
    @Test void examples() {
        char[][] b = g("XXXX", "XOOX", "XXOX", "XOXX");
        new SurroundedRegions().solve(b);
        assertArrayEquals(g("XXXX", "XXXX", "XXXX", "XOXX"), b);
        char[][] b2 = g("OO", "OO");
        new SurroundedRegions().solve(b2);
        assertArrayEquals(g("OO", "OO"), b2);
    }
}
```
