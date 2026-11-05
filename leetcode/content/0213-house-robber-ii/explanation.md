# 0213. House Robber II

**Difficulty:** Medium | **Category:** 1-D Dynamic Programming | **LeetCode:** https://leetcode.com/problems/house-robber-ii/

## Problem
- Same as House Robber, but the houses form a circle: the first and last are adjacent.

## Intuition
- The first and last houses cannot both be robbed. So solve two linear problems: houses [0..n-2] and [1..n-1], and take the max.

## Brute Force
- Enumerate subsets with a circular adjacency check: O(2^n).

## Optimal Approach
1. If n == 1 return nums[0].
2. Return max(rob(0, n-2), rob(1, n-1)) using the linear solver.

## Worked Example
- [2,3,2].
```text
exclude last : [2,3] -> 3
exclude first: [3,2] -> 3
answer 3
```

## Complexity
- Time: O(n). Space: O(1).

## Pitfalls
- n == 1: both ranges would be empty, so special-case it.

## Video Script
- Reduce a new problem to an old one: break the circle.

## Solution
```java file=dp1/HouseRobberII.java
package dp1;

/**
 * LC 213 House Robber II.
 * Approach: circle -> max of two linear robberies excluding first or last house.
 * Time O(n), Space O(1).
 */
public class HouseRobberII {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        HouseRobber linear = new HouseRobber();
        return Math.max(linear.rob(nums, 0, n - 2), linear.rob(nums, 1, n - 1));
    }
}
```

## Tests
```java test=dp1/HouseRobberIITest.java
package dp1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class HouseRobberIITest {
    HouseRobberII s = new HouseRobberII();
    @Test void examples() {
        assertEquals(3, s.rob(new int[]{2, 3, 2}));
        assertEquals(4, s.rob(new int[]{1, 2, 3, 1}));
        assertEquals(3, s.rob(new int[]{1, 2, 3}));
        assertEquals(7, s.rob(new int[]{7}));
    }
}
```
