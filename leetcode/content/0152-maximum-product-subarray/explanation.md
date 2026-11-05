# 0152. Maximum Product Subarray

**Difficulty:** Medium | **Category:** 1-D Dynamic Programming | **LeetCode:** https://leetcode.com/problems/maximum-product-subarray/

## Problem
- Return the largest product of a contiguous non-empty subarray.

## Intuition
- A negative number flips the biggest product into the smallest and vice versa.
- Track both the max and the min product ending at each index.

## Brute Force
- All subarrays: O(n^2).

## Optimal Approach
1. hi = lo = best = nums[0].
2. For x: candidates x, hi*x, lo*x; hi = max, lo = min; best = max(best, hi).

## Worked Example
- [2,3,-2,4].
```text
x=2  hi=2  lo=2   best=2
x=3  hi=6  lo=3   best=6
x=-2 hi=-2 lo=-12 best=6
x=4  hi=4  lo=-48 best=6
```
- [-2,3,-4]: hi ends at 24 because lo (-6) times -4 = 24.

## Complexity
- Time: O(n). Space: O(1).

## Pitfalls
- Compute the new hi and lo from the old values simultaneously (use temps).
- Zero resets both, which the "x alone" candidate handles.

## Video Script
- Kadane's algorithm with a twist: two running values.

## Solution
```java file=dp1/MaximumProductSubarray.java
package dp1;

/**
 * LC 152 Maximum Product Subarray.
 * Approach: track max and min product ending here (negatives swap them).
 * Time O(n), Space O(1).
 */
public class MaximumProductSubarray {
    public int maxProduct(int[] nums) {
        int hi = nums[0], lo = nums[0], best = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int x = nums[i], a = hi * x, b = lo * x;
            hi = Math.max(x, Math.max(a, b));
            lo = Math.min(x, Math.min(a, b));
            best = Math.max(best, hi);
        }
        return best;
    }
}
```

## Tests
```java test=dp1/MaximumProductSubarrayTest.java
package dp1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MaximumProductSubarrayTest {
    MaximumProductSubarray s = new MaximumProductSubarray();
    @Test void examples() {
        assertEquals(6, s.maxProduct(new int[]{2, 3, -2, 4}));
        assertEquals(0, s.maxProduct(new int[]{-2, 0, -1}));
        assertEquals(24, s.maxProduct(new int[]{-2, 3, -4}));
        assertEquals(-2, s.maxProduct(new int[]{-2}));
    }
}
```
