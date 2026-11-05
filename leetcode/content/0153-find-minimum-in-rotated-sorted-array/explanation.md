# 0153. Find Minimum in Rotated Sorted Array

**Difficulty:** Medium | **Category:** Binary Search | **LeetCode:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

## Problem
- A sorted array of distinct values was rotated. Return its minimum in O(log n).
- Example: [3,4,5,1,2] -> 1.

## Intuition
- Compare nums[mid] with nums[hi]. If nums[mid] > nums[hi], the drop (and the minimum) lies to the right of mid.
- Otherwise mid..hi is sorted, so the minimum is at mid or to its left.

## Brute Force
- Linear scan for the min: O(n).

## Optimal Approach
1. lo = 0, hi = n-1.
2. While lo < hi: mid; if nums[mid] > nums[hi], lo = mid+1; else hi = mid.
3. Return nums[lo].

## Worked Example
- [4,5,6,7,0,1,2].
```text
lo=0 hi=6 mid=3 (7) > 2 -> lo=4
lo=4 hi=6 mid=5 (1) <= 2 -> hi=5
lo=4 hi=5 mid=4 (0) <= 1 -> hi=4
answer nums[4] = 0
```

## Complexity
- Time: O(log n). Space: O(1).

## Pitfalls
- Comparing with nums[lo] instead of nums[hi] fails on an unrotated array unless handled specially.
- hi = mid (not mid-1): mid could be the minimum.

## Video Script
- Draw the rotated array as two ascending ramps; mid tells you which ramp you are on.

## Solution
```java file=binarysearch/FindMinimumInRotatedSortedArray.java
package binarysearch;

/**
 * LC 153 Find Minimum in Rotated Sorted Array.
 * Approach: compare mid with hi; the minimum is in the unsorted half.
 * Time O(log n), Space O(1).
 */
public class FindMinimumInRotatedSortedArray {
    public int findMin(int[] nums) {
        int lo = 0, hi = nums.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] > nums[hi]) lo = mid + 1;
            else hi = mid;
        }
        return nums[lo];
    }
}
```

## Tests
```java test=binarysearch/FindMinimumInRotatedSortedArrayTest.java
package binarysearch;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class FindMinimumInRotatedSortedArrayTest {
    FindMinimumInRotatedSortedArray s = new FindMinimumInRotatedSortedArray();
    @Test void examples() {
        assertEquals(1, s.findMin(new int[]{3, 4, 5, 1, 2}));
        assertEquals(0, s.findMin(new int[]{4, 5, 6, 7, 0, 1, 2}));
        assertEquals(11, s.findMin(new int[]{11, 13, 15, 17}));
        assertEquals(1, s.findMin(new int[]{2, 1}));
        assertEquals(5, s.findMin(new int[]{5}));
    }
}
```
