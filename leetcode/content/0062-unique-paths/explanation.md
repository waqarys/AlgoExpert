# 0062. Unique Paths

**Difficulty:** Medium | **Category:** 2-D Dynamic Programming | **LeetCode:** https://leetcode.com/problems/unique-paths/

## Problem
- A robot moves only right or down on an m x n grid from the top-left to the bottom-right. Count the paths.

## Intuition
- paths(r, c) = paths(r-1, c) + paths(r, c-1). The first row and column have exactly 1 path.
- One row of the table is enough. (Closed form: C(m+n-2, m-1).)

## Brute Force
- Recursion without memo: O(2^(m+n)).

## Optimal Approach
1. row = [1] * n.
2. For each of the remaining m-1 rows: for c = 1..n-1: row[c] += row[c-1].

## Worked Example
- m = 3, n = 7.
```text
row0: 1 1 1 1  1  1  1
row1: 1 2 3 4  5  6  7
row2: 1 3 6 10 15 21 28   -> 28
```

## Complexity
- Time: O(m * n). Space: O(n).

## Pitfalls
- The combinatorial formula overflows int quickly; use long and incremental division if you go that way.

## Video Script
- First 2-D DP: draw the grid and fill it live.

## Solution
```java file=dp2/UniquePaths.java
package dp2;

import java.util.*;

/**
 * LC 62 Unique Paths.
 * Approach: grid DP compressed to one row: row[c] += row[c-1].
 * Time O(mn), Space O(n).
 */
public class UniquePaths {
    public int uniquePaths(int m, int n) {
        int[] row = new int[n];
        Arrays.fill(row, 1);
        for (int r = 1; r < m; r++)
            for (int c = 1; c < n; c++) row[c] += row[c - 1];
        return row[n - 1];
    }
}
```

## Tests
```java test=dp2/UniquePathsTest.java
package dp2;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class UniquePathsTest {
    UniquePaths s = new UniquePaths();
    @Test void examples() {
        assertEquals(28, s.uniquePaths(3, 7));
        assertEquals(3, s.uniquePaths(3, 2));
        assertEquals(1, s.uniquePaths(1, 1));
        assertEquals(1, s.uniquePaths(1, 10));
    }
}
```
