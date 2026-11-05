# 0416. Partition Equal Subset Sum

**Difficulty:** Medium | **Category:** 1-D Dynamic Programming | **LeetCode:** https://leetcode.com/problems/partition-equal-subset-sum/

## Problem
- Can the array be split into two subsets with equal sums?

## Intuition
- Equivalent to: is there a subset summing to total / 2? (total must be even.)
- 0/1 knapsack on a boolean array: can[s] = can we reach sum s with the items so far.

## Brute Force
- Try all subsets: O(2^n).

## Optimal Approach
1. If total is odd return false; target = total / 2.
2. can[0] = true. For each x, for s from target down to x: can[s] |= can[s - x].
3. Return can[target].

## Worked Example
- [1,5,11,5], target 11.
```text
x=1  reach {0,1}
x=5  reach {0,1,5,6}
x=11 reach {0,1,5,6,11,...}  -> 11 reachable -> true
```

## Complexity
- Time: O(n * target). Space: O(target).

## Pitfalls
- Iterate s downwards so each item is used at most once.

## Video Script
- Introduce 0/1 knapsack and why the loop direction matters.

## Solution
```java file=dp1/PartitionEqualSubsetSum.java
package dp1;

/**
 * LC 416 Partition Equal Subset Sum.
 * Approach: 0/1 knapsack boolean DP for total/2, iterating sums downward.
 * Time O(n * sum), Space O(sum).
 */
public class PartitionEqualSubsetSum {
    public boolean canPartition(int[] nums) {
        int total = 0;
        for (int x : nums) total += x;
        if (total % 2 == 1) return false;
        int target = total / 2;
        boolean[] can = new boolean[target + 1];
        can[0] = true;
        for (int x : nums)
            for (int s = target; s >= x; s--) can[s] |= can[s - x];
        return can[target];
    }
}
```

## Tests
```java test=dp1/PartitionEqualSubsetSumTest.java
package dp1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class PartitionEqualSubsetSumTest {
    PartitionEqualSubsetSum s = new PartitionEqualSubsetSum();
    @Test void examples() {
        assertTrue(s.canPartition(new int[]{1, 5, 11, 5}));
        assertFalse(s.canPartition(new int[]{1, 2, 3, 5}));
        assertFalse(s.canPartition(new int[]{2}));
        assertTrue(s.canPartition(new int[]{3, 3}));
    }
}
```
