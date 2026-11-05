# 0051. N-Queens

**Difficulty:** Hard | **Category:** Backtracking | **LeetCode:** https://leetcode.com/problems/n-queens/

## Problem
- Place n queens on an n x n board so none attack each other. Return all boards ("Q" and ".").

## Intuition
- Exactly one queen per row, so recurse row by row and choose a column.
- A column is safe if no earlier queen shares its column, its "/" diagonal (r + c) or its "\" diagonal (r - c).
- Three boolean sets make each safety check O(1).

## Brute Force
- Try all C(n^2, n) placements and validate: astronomically slow.

## Optimal Approach
1. cols[], diag1[r+c], diag2[r-c+n-1].
2. place(r): if r == n record board.
3. For c: if all three are free, mark, set board[r][c] = 'Q', place(r+1), unmark.

## Worked Example
- n = 4 (one solution path).
```text
r0 c1  .Q..
r1 c3  ...Q
r2 c0  Q...
r3 c2  ..Q.   -> solution
(the other solution is the mirror: c2, c0, c3, c1)
```

## Complexity
- Time: O(n!) roughly. Space: O(n^2) for the board.

## Pitfalls
- Offset r - c by n - 1 so the index is non-negative.

## Video Script
- Classic backtracking showcase; animate queens and the attacked diagonals.

## Solution
```java file=backtracking/NQueens.java
package backtracking;

import java.util.*;

/**
 * LC 51 N-Queens.
 * Approach: row-by-row backtracking with column and two diagonal occupancy arrays.
 * Time O(n!), Space O(n^2).
 */
public class NQueens {
    public List<List<String>> solveNQueens(int n) {
        char[][] board = new char[n][n];
        for (char[] row : board) Arrays.fill(row, '.');
        List<List<String>> res = new ArrayList<>();
        place(0, n, board, new boolean[n], new boolean[2 * n], new boolean[2 * n], res);
        return res;
    }

    private void place(int r, int n, char[][] b, boolean[] cols, boolean[] d1, boolean[] d2, List<List<String>> res) {
        if (r == n) {
            List<String> sol = new ArrayList<>();
            for (char[] row : b) sol.add(new String(row));
            res.add(sol);
            return;
        }
        for (int c = 0; c < n; c++) {
            if (cols[c] || d1[r + c] || d2[r - c + n - 1]) continue;
            cols[c] = d1[r + c] = d2[r - c + n - 1] = true;
            b[r][c] = 'Q';
            place(r + 1, n, b, cols, d1, d2, res);
            b[r][c] = '.';
            cols[c] = d1[r + c] = d2[r - c + n - 1] = false;
        }
    }
}
```

## Tests
```java test=backtracking/NQueensTest.java
package backtracking;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class NQueensTest {
    NQueens s = new NQueens();
    @Test void examples() {
        assertEquals(List.of(List.of(".Q..", "...Q", "Q...", "..Q."), List.of("..Q.", "Q...", "...Q", ".Q..")), s.solveNQueens(4));
        assertEquals(List.of(List.of("Q")), s.solveNQueens(1));
        assertEquals(92, s.solveNQueens(8).size());
        assertEquals(0, s.solveNQueens(3).size());
    }
}
```
