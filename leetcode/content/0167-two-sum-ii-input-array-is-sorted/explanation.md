# 0167. Two Sum II - Input Array Is Sorted

**Difficulty:** Medium | **Category:** Two Pointers | **LeetCode:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

## Problem
- numbers is sorted ascending. Return 1-indexed positions [i, j] with numbers[i] + numbers[j] == target, using O(1) extra space.
- Example: [2,7,11,15], target 9 -> [1,2].

## Intuition
- Sorted order lets us steer: if the sum is too small, the only way to grow it is to move the left pointer right; if too big, move the right pointer left.
- Each move discards a whole row/column of impossible pairs, so we never miss the answer.

## Brute Force
- All pairs O(n^2), or a HashMap like Two Sum (O(n) space, violates the constraint).

## Optimal Approach
1. l = 0, r = n-1.
2. sum = a[l] + a[r]. Equal -> return [l+1, r+1]. Less -> l++. Greater -> r--.

## Worked Example
- numbers = [2, 3, 4], target = 6.
```text
l=0(2) r=2(4) sum=6 -> return [1,3]
```
- numbers = [1,3,4,5,7,11], target = 9:
```text
1+11=12 > 9 -> r--
1+7 = 8 < 9 -> l++
3+7 =10 > 9 -> r--
3+5 = 8 < 9 -> l++
4+5 = 9 -> [3,4]
```

## Complexity
- Time: O(n). Space: O(1).

## Pitfalls
- Answer is 1-indexed.
- Use the sorted property; a HashMap is not accepted for the O(1) space requirement.

## Video Script
- Draw the sum matrix to prove why moving a pointer safely eliminates candidates.

## Solution
```java file=twopointers/TwoSumII.java
package twopointers;

/**
 * LC 167 Two Sum II (sorted input).
 * Approach: converging two pointers; move l up if the sum is small, r down if large.
 * Time O(n), Space O(1).
 */
public class TwoSumII {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0, r = numbers.length - 1;
        while (l < r) {
            int sum = numbers[l] + numbers[r];
            if (sum == target) return new int[]{l + 1, r + 1};
            if (sum < target) l++;
            else r--;
        }
        return new int[0];
    }
}
```

## Tests
```java test=twopointers/TwoSumIITest.java
package twopointers;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TwoSumIITest {
    TwoSumII s = new TwoSumII();
    @Test void examples() {
        assertArrayEquals(new int[]{1, 2}, s.twoSum(new int[]{2, 7, 11, 15}, 9));
        assertArrayEquals(new int[]{1, 3}, s.twoSum(new int[]{2, 3, 4}, 6));
        assertArrayEquals(new int[]{1, 2}, s.twoSum(new int[]{-1, 0}, -1));
        assertArrayEquals(new int[]{3, 4}, s.twoSum(new int[]{1, 3, 4, 5, 7, 11}, 9));
    }
}
```
