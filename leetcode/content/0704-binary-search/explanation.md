# 0704. Binary Search

**Difficulty:** Easy | **Category:** Binary Search | **LeetCode:** https://leetcode.com/problems/binary-search/

## Problem
- Find target in a sorted array of distinct integers; return its index or -1, in O(log n).

## Intuition
- Compare with the middle element; half of the remaining range can be discarded each step.

## Brute Force
- Linear scan: O(n).

## Optimal Approach
1. lo = 0, hi = n-1.
2. mid = lo + (hi - lo) / 2.
3. Equal -> return mid; a[mid] < target -> lo = mid+1; else hi = mid-1.

## Worked Example
- nums = [-1,0,3,5,9,12], target = 9.
```text
lo=0 hi=5 mid=2 (3)  < 9 -> lo=3
lo=3 hi=5 mid=4 (9)  found -> 4
```

## Complexity
- Time: O(log n). Space: O(1).

## Pitfalls
- (lo + hi) / 2 can overflow; use lo + (hi - lo) / 2.
- Loop condition lo <= hi for the closed interval [lo, hi].

## Video Script
- Teach the invariant "if target exists, it is in [lo, hi]" - every template in this section builds on it.

## Solution
```java file=binarysearch/BinarySearch.java
package binarysearch;

/**
 * LC 704 Binary Search.
 * Approach: closed interval [lo, hi], halve each step.
 * Time O(log n), Space O(1).
 */
public class BinarySearch {
    public int search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return -1;
    }
}
```

## Tests
```java test=binarysearch/BinarySearchTest.java
package binarysearch;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class BinarySearchTest {
    BinarySearch s = new BinarySearch();
    @Test void examples() {
        assertEquals(4, s.search(new int[]{-1, 0, 3, 5, 9, 12}, 9));
        assertEquals(-1, s.search(new int[]{-1, 0, 3, 5, 9, 12}, 2));
        assertEquals(0, s.search(new int[]{5}, 5));
        assertEquals(-1, s.search(new int[]{}, 5));
    }
}
```
