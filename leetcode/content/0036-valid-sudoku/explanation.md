# 0036. Valid Sudoku

**Difficulty:** Medium | **Category:** Arrays & Hashing | **LeetCode:** https://leetcode.com/problems/valid-sudoku/

## Problem
- Decide whether a partially filled 9x9 Sudoku board is valid: no digit repeats in any row, column, or 3x3 box.
- Empty cells are '.'. The board need not be solvable.

## Intuition
- Each filled cell belongs to exactly one row, one column and one box.
- Track seen digits per row, column and box; box index = (r/3)*3 + c/3.
- A single scan finds any conflict.

## Brute Force
- Check each row, each column and each box separately with a fresh set: 27 passes of 9 cells. Still O(81) but more code.

## Optimal Approach
1. Keep boolean[9][9] rows, cols, boxes (digit seen?).
2. For each filled cell (r, c, d): b = (r/3)*3 + c/3.
3. If rows[r][d] or cols[c][d] or boxes[b][d] is already true, return false; else set all three.

## Worked Example
- Suppose the board has '8' at (0,0) and another '8' at (2,2) (classic invalid example).
```text
(0,0) d=8 box=0 -> mark row0, col0, box0
...
(2,2) d=8 box=(2/3)*3+2/3 = 0 -> box0 already has 8 -> return false
```

## Complexity
- Time: O(81) = O(1) for a fixed board; O(n^2) for an n x n generalisation.
- Space: O(1) (three 9x9 tables).

## Pitfalls
- Getting the box formula wrong; test it on corners (0,0)->0, (8,8)->8, (4,7)->5.
- Do not try to solve the puzzle, only validate.

## Video Script
- Show the three rules, then show that one cell participates in three "groups".
- Derive the box index formula visually on a 9x9 grid.

## Solution
```java file=arrays/ValidSudoku.java
package arrays;

/**
 * LC 36 Valid Sudoku.
 * Approach: one scan with seen-tables for rows, columns and boxes; box = (r/3)*3 + c/3.
 * Time O(1) for 9x9, Space O(1).
 */
public class ValidSudoku {
    public boolean isValidSudoku(char[][] board) {
        boolean[][] rows = new boolean[9][9], cols = new boolean[9][9], boxes = new boolean[9][9];
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char ch = board[r][c];
                if (ch == '.') continue;
                int d = ch - '1', b = (r / 3) * 3 + c / 3;
                if (rows[r][d] || cols[c][d] || boxes[b][d]) return false;
                rows[r][d] = cols[c][d] = boxes[b][d] = true;
            }
        }
        return true;
    }
}
```

## Tests
```java test=arrays/ValidSudokuTest.java
package arrays;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ValidSudokuTest {
    static char[][] b(String... rows) {
        char[][] g = new char[9][];
        for (int i = 0; i < 9; i++) g[i] = rows[i].toCharArray();
        return g;
    }
    static final String[] VALID = {"53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1",
            "7...2...6", ".6....28.", "...419..5", "....8..79"};
    @Test void valid() { assertTrue(new ValidSudoku().isValidSudoku(b(VALID))); }
    @Test void boxConflict() {
        String[] r = VALID.clone();
        r[0] = "83..7....";
        r[3] = "....6...3"; // remove the column clash so only the box rule fires
        r[2] = "..8....6.";
        assertFalse(new ValidSudoku().isValidSudoku(b(r)));
    }
    @Test void rowConflict() {
        String[] r = VALID.clone();
        r[0] = "53..7..5.";
        assertFalse(new ValidSudoku().isValidSudoku(b(r)));
    }
}
```
