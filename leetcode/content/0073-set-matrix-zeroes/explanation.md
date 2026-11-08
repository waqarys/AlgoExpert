# 0073. Set Matrix Zeroes

**Difficulty:** Medium | **Category:** Math & Geometry | **LeetCode:** https://leetcode.com/problems/set-matrix-zeroes/

## Problem
- If an element is 0, set its entire row and column to 0, in place. Follow-up: O(1) extra space.

## Intuition
- Use the first row and first column as marker arrays. Two booleans remember whether the first row and column themselves must be zeroed.

## Brute Force
- Copy the matrix: O(mn) space. Row and column boolean arrays: O(m + n) space.

## Optimal Approach
1. firstRow / firstCol = whether they contain a zero.
2. For r, c >= 1: if m[r][c] == 0, set m[r][0] = m[0][c] = 0.
3. For r, c >= 1: zero the cell if m[r][0] == 0 or m[0][c] == 0.
4. Zero the first row and column if their flags are set.

## Worked Example
- [[0,1,2,0],[3,4,5,2],[1,3,1,5]].
```text
firstRow has a zero -> true ; firstCol has a zero -> true
inner cells in columns 0 and 3 -> 0
finally zero row 0 and column 0
result [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

## Complexity
- Time: O(m * n). Space: O(1).

## Pitfalls
- Process the first row and column last, or the markers overwrite real data too early.

## Video Script
- "Use the matrix as its own notebook."

## Solution
```java file=math/SetMatrixZeroes.java
package math;

/**
 * LC 73 Set Matrix Zeroes.
 * Approach: first row/column as markers plus two flags.
 * Time O(mn), Space O(1).
 */
public class SetMatrixZeroes {
    public void setZeroes(int[][] m) {
        int rows = m.length, cols = m[0].length;
        boolean firstRow = false, firstCol = false;
        for (int c = 0; c < cols; c++) if (m[0][c] == 0) firstRow = true;
        for (int r = 0; r < rows; r++) if (m[r][0] == 0) firstCol = true;
        for (int r = 1; r < rows; r++)
            for (int c = 1; c < cols; c++)
                if (m[r][c] == 0) { m[r][0] = 0; m[0][c] = 0; }
        for (int r = 1; r < rows; r++)
            for (int c = 1; c < cols; c++)
                if (m[r][0] == 0 || m[0][c] == 0) m[r][c] = 0;
        if (firstRow) for (int c = 0; c < cols; c++) m[0][c] = 0;
        if (firstCol) for (int r = 0; r < rows; r++) m[r][0] = 0;
    }
}
```

## Tests
```java test=math/SetMatrixZeroesTest.java
package math;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SetMatrixZeroesTest {
    @Test void examples() {
        int[][] a = {{1, 1, 1}, {1, 0, 1}, {1, 1, 1}};
        new SetMatrixZeroes().setZeroes(a);
        assertArrayEquals(new int[][]{{1, 0, 1}, {0, 0, 0}, {1, 0, 1}}, a);
        int[][] b = {{0, 1, 2, 0}, {3, 4, 5, 2}, {1, 3, 1, 5}};
        new SetMatrixZeroes().setZeroes(b);
        assertArrayEquals(new int[][]{{0, 0, 0, 0}, {0, 4, 5, 0}, {0, 3, 1, 0}}, b);
    }
}
```
