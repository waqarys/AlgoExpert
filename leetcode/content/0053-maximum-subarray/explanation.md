# 0053. Maximum Subarray

**Difficulty:** Medium | **Category:** Greedy | **LeetCode:** https://leetcode.com/problems/maximum-subarray/

## Problem
- Return the largest sum of a contiguous non-empty subarray.

## Intuition
- Kadane's algorithm: a running sum that has gone negative can only hurt whatever comes next, so drop it and start fresh.

## Brute Force
- All subarrays: O(n^2) with running sums.

## Optimal Approach
1. cur = 0, best = -infinity.
2. For x: cur = max(x, cur + x); best = max(best, cur).

## Worked Example
- [-2,1,-3,4,-1,2,1,-5,4].
```text
cur : -2  1 -2  4  3  5  6  1  5
best: -2  1  1  4  4  5  6  6  6
answer 6 ([4,-1,2,1])
```

## Complexity
- Time: O(n). Space: O(1).

## Pitfalls
- All-negative input: the answer is the largest element, so do not start best at 0.

## Video Script
- Kadane in one sentence: "extend or restart".

## Solution
```java file=greedy/MaximumSubarray.java
package greedy;

/**
 * LC 53 Maximum Subarray.
 * Approach: Kadane - extend the running sum or restart at x.
 * Time O(n), Space O(1).
 */
public class MaximumSubarray {
    public int maxSubArray(int[] nums) {
        int cur = 0, best = Integer.MIN_VALUE;
        for (int x : nums) {
            cur = Math.max(x, cur + x);
            best = Math.max(best, cur);
        }
        return best;
    }
}
```

## Tests
```java test=greedy/MaximumSubarrayTest.java
package greedy;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MaximumSubarrayTest {
    MaximumSubarray s = new MaximumSubarray();
    @Test void examples() {
        assertEquals(6, s.maxSubArray(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4}));
        assertEquals(1, s.maxSubArray(new int[]{1}));
        assertEquals(23, s.maxSubArray(new int[]{5, 4, -1, 7, 8}));
        assertEquals(-1, s.maxSubArray(new int[]{-3, -1, -2}));
    }
}
```
