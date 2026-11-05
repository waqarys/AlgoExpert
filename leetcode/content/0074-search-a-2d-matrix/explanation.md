# 0074. Search a 2D Matrix

**Difficulty:** Medium | **Category:** Binary Search | **LeetCode:** https://leetcode.com/problems/search-a-2d-matrix/

## Problem
- Rows are sorted, and each row's first value is greater than the previous row's last. Is target present? Do it in O(log(m*n)).

## Intuition
- Reading the matrix row by row gives one sorted array of length m*n.
- Index k maps to cell (k / n, k % n), so we can binary search the virtual array directly.

## Brute Force
- Scan every cell: O(m*n). Binary search each row: O(m log n).

## Optimal Approach
1. lo = 0, hi = m*n - 1.
2. mid -> v = matrix[mid / n][mid % n]; compare as in standard binary search.

## Worked Example
- matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target 3.
```text
lo=0 hi=11 mid=5 -> (1,1)=11 > 3 -> hi=4
lo=0 hi=4  mid=2 -> (0,2)=5  > 3 -> hi=1
lo=0 hi=1  mid=0 -> (0,0)=1  < 3 -> lo=1
lo=1 hi=1  mid=1 -> (0,1)=3  found
```

## Complexity
- Time: O(log(m*n)). Space: O(1).

## Pitfalls
- Divide and mod by the number of columns n, not rows.

## Video Script
- Animate "unrolling" the matrix into one array; then it is problem 704.

## Solution
```java file=binarysearch/SearchA2DMatrix.java
package binarysearch;

/**
 * LC 74 Search a 2D Matrix.
 * Approach: binary search over the virtual flattened array, index k -> (k / n, k % n).
 * Time O(log(mn)), Space O(1).
 */
public class SearchA2DMatrix {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length, lo = 0, hi = m * n - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2, v = matrix[mid / n][mid % n];
            if (v == target) return true;
            if (v < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return false;
    }
}
```

## Tests
```java test=binarysearch/SearchA2DMatrixTest.java
package binarysearch;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SearchA2DMatrixTest {
    SearchA2DMatrix s = new SearchA2DMatrix();
    int[][] m = {{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}};
    @Test void examples() {
        assertTrue(s.searchMatrix(m, 3));
        assertFalse(s.searchMatrix(m, 13));
        assertTrue(s.searchMatrix(m, 60));
        assertFalse(s.searchMatrix(new int[][]{{1}}, 2));
    }
}
```
