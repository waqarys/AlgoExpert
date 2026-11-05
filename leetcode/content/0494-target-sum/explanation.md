# 0494. Target Sum

**Difficulty:** Medium | **Category:** 2-D Dynamic Programming | **LeetCode:** https://leetcode.com/problems/target-sum/

## Problem
- Put + or - before each number. Count the assignments whose total equals target.

## Intuition
- Let P be the numbers with +. Then sum(P) - (total - sum(P)) = target, so sum(P) = (total + target) / 2.
- The problem becomes "count subsets with a given sum": 0/1 knapsack counting.

## Brute Force
- Try all 2^n sign assignments (or memoise on (index, running sum)).

## Optimal Approach
1. If |target| > total or (total + target) is odd, return 0.
2. s = (total + target) / 2; ways[0] = 1.
3. For each x: for t from s down to x: ways[t] += ways[t - x].

## Worked Example
- nums [1,1,1,1,1], target 3.
```text
total=5 -> s=(5+3)/2=4
count subsets of five 1s with sum 4 = C(5,4) = 5
```

## Complexity
- Time: O(n * s). Space: O(s).

## Pitfalls
- Zeros double the count (+0 and -0); the DP handles it because x = 0 adds ways[t] to itself once per zero.

## Video Script
- Algebra trick turns an exponential search into knapsack - a great "aha" moment.

## Solution
```java file=dp2/TargetSum.java
package dp2;

/**
 * LC 494 Target Sum.
 * Approach: reduce to counting subsets with sum (total + target) / 2 (0/1 knapsack).
 * Time O(n * sum), Space O(sum).
 */
public class TargetSum {
    public int findTargetSumWays(int[] nums, int target) {
        int total = 0;
        for (int x : nums) total += x;
        if (Math.abs(target) > total || (total + target) % 2 != 0) return 0;
        int s = (total + target) / 2;
        int[] ways = new int[s + 1];
        ways[0] = 1;
        for (int x : nums)
            for (int t = s; t >= x; t--) ways[t] += ways[t - x];
        return ways[s];
    }
}
```

## Tests
```java test=dp2/TargetSumTest.java
package dp2;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TargetSumTest {
    TargetSum s = new TargetSum();
    @Test void examples() {
        assertEquals(5, s.findTargetSumWays(new int[]{1, 1, 1, 1, 1}, 3));
        assertEquals(1, s.findTargetSumWays(new int[]{1}, 1));
        assertEquals(2, s.findTargetSumWays(new int[]{0, 1}, 1));
        assertEquals(0, s.findTargetSumWays(new int[]{1, 2}, 4));
        assertEquals(1, s.findTargetSumWays(new int[]{1, 2}, -3));
    }
}
```
