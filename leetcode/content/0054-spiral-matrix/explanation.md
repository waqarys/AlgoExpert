# 0054. Spiral Matrix

**Difficulty:** Medium | **Category:** Math & Geometry | **LeetCode:** https://leetcode.com/problems/spiral-matrix/

## Problem
- Return all elements of an m x n matrix in clockwise spiral order.

## Intuition
- Keep four boundaries (top, bottom, left, right). Walk the top row, right column, bottom row and left column, shrinking a boundary after each side.

## Brute Force
- Simulate with direction changes and a visited matrix: O(mn) time and extra space.

## Optimal Approach
1. While top <= bottom and left <= right:
2. Top row left to right; top++. Right column top to bottom; right--.
3. If top <= bottom: bottom row right to left; bottom--. If left <= right: left column bottom to top; left++.

## Worked Example
```text
1  2  3  4
5  6  7  8     -> 1 2 3 4 8 12 11 10 9 5 6 7
9 10 11 12
```

## Complexity
- Time: O(m * n). Space: O(1) besides the output.

## Pitfalls
- The two inner checks prevent visiting a single remaining row or column twice.

## Video Script
- Animate the boundaries closing in like a camera aperture.

## Solution
```java file=math/SpiralMatrix.java
package math;

import java.util.*;

/**
 * LC 54 Spiral Matrix.
 * Approach: shrink four boundaries after walking each side.
 * Time O(mn), Space O(1) extra.
 */
public class SpiralMatrix {
    public List<Integer> spiralOrder(int[][] m) {
        List<Integer> res = new ArrayList<>();
        int top = 0, bottom = m.length - 1, left = 0, right = m[0].length - 1;
        while (top <= bottom && left <= right) {
            for (int c = left; c <= right; c++) res.add(m[top][c]);
            top++;
            for (int r = top; r <= bottom; r++) res.add(m[r][right]);
            right--;
            if (top <= bottom) {
                for (int c = right; c >= left; c--) res.add(m[bottom][c]);
                bottom--;
            }
            if (left <= right) {
                for (int r = bottom; r >= top; r--) res.add(m[r][left]);
                left++;
            }
        }
        return res;
    }
}
```

## Tests
```java test=math/SpiralMatrixTest.java
package math;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class SpiralMatrixTest {
    SpiralMatrix s = new SpiralMatrix();
    @Test void examples() {
        assertEquals(List.of(1, 2, 3, 6, 9, 8, 7, 4, 5), s.spiralOrder(new int[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}));
        assertEquals(List.of(1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7), s.spiralOrder(new int[][]{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}}));
        assertEquals(List.of(1, 2, 3), s.spiralOrder(new int[][]{{1}, {2}, {3}}));
    }
}
```
