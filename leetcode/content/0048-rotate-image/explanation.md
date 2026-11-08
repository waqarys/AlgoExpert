# 0048. Rotate Image

**Difficulty:** Medium | **Category:** Math & Geometry | **LeetCode:** https://leetcode.com/problems/rotate-image/

## Problem
- Rotate an n x n matrix 90 degrees clockwise, in place.

## Intuition
- A clockwise rotation equals a transpose (swap across the main diagonal) followed by reversing each row.

## Brute Force
- Copy into a new matrix with res[c][n-1-r] = m[r][c]: O(n^2) extra space, which is not allowed.

## Optimal Approach
1. Transpose: for r < c swap m[r][c] and m[c][r].
2. Reverse every row.

## Worked Example
```text
1 2 3     transpose     1 4 7     reverse rows     7 4 1
4 5 6        ->         2 5 8          ->          8 5 2
7 8 9                   3 6 9                      9 6 3
```

## Complexity
- Time: O(n^2). Space: O(1).

## Pitfalls
- In the transpose, only swap for c > r, or the second swap undoes the first.

## Video Script
- Show the two-step trick on a coloured 3x3, then mention the four-way cycle swap alternative.

## Solution
```java file=math/RotateImage.java
package math;

/**
 * LC 48 Rotate Image.
 * Approach: transpose then reverse each row.
 * Time O(n^2), Space O(1).
 */
public class RotateImage {
    public void rotate(int[][] m) {
        int n = m.length;
        for (int r = 0; r < n; r++)
            for (int c = r + 1; c < n; c++) { int t = m[r][c]; m[r][c] = m[c][r]; m[c][r] = t; }
        for (int[] row : m)
            for (int l = 0, r = n - 1; l < r; l++, r--) { int t = row[l]; row[l] = row[r]; row[r] = t; }
    }
}
```

## Tests
```java test=math/RotateImageTest.java
package math;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class RotateImageTest {
    @Test void examples() {
        int[][] m = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        new RotateImage().rotate(m);
        assertArrayEquals(new int[][]{{7, 4, 1}, {8, 5, 2}, {9, 6, 3}}, m);
        int[][] m2 = {{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}};
        new RotateImage().rotate(m2);
        assertArrayEquals(new int[][]{{15, 13, 2, 5}, {14, 3, 4, 1}, {12, 6, 8, 9}, {16, 7, 10, 11}}, m2);
    }
}
```
