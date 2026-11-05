# 0001. Two Sum

**Difficulty:** Easy | **Category:** Arrays & Hashing | **LeetCode:** https://leetcode.com/problems/two-sum/

## Problem
- Given nums and target, return the indices of the two numbers that add up to target.
- Exactly one solution exists, and you may not use the same element twice.
- Example: nums = [2,7,11,15], target = 9 -> [0,1].

## Intuition
- For each x, the partner we need is target - x (its complement).
- If we remember every value we have already passed (value -> index), we can check for the complement in O(1).

## Brute Force
- Try every pair i < j and test nums[i] + nums[j] == target: O(n^2) time, O(1) space.

## Optimal Approach
1. Keep a HashMap from value to index.
2. For index i with value x: if map contains target - x, return [map.get(target - x), i].
3. Otherwise store x -> i and continue.
4. Checking before inserting guarantees we never pair an element with itself.

## Worked Example
- nums = [3, 2, 4], target = 6.
```text
i=0 x=3 need 3  map={}          -> store 3:0
i=1 x=2 need 4  map={3:0}       -> store 2:1
i=2 x=4 need 2  map={3:0,2:1}   -> found at 1 -> return [1,2]
```

## Complexity
- Time: O(n), one pass.
- Space: O(n) for the map.

## Pitfalls
- Inserting before checking breaks cases like [3,3] target 6 only if you overwrite; checking first is the clean fix.
- Return indices, not values. Sorting destroys the original indices.

## Video Script
- Hook: "LeetCode problem number one, and the most common warm-up question in interviews."
- Brute force pairs, then the complement idea, then the one-pass map.
- Trace [3,2,4] to show why we check before we insert.

## Solution
```java file=arrays/TwoSum.java
package arrays;

import java.util.*;

/**
 * LC 1 Two Sum. Indices of two numbers summing to target.
 * Approach: one-pass HashMap of value -> index; look up the complement before inserting.
 * Time O(n), Space O(n).
 */
public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> index = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            Integer j = index.get(target - nums[i]);
            if (j != null) return new int[]{j, i};
            index.put(nums[i], i);
        }
        return new int[0];
    }

    /** Brute force for comparison. O(n^2). */
    public int[] twoSumBrute(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++)
            for (int j = i + 1; j < nums.length; j++)
                if (nums[i] + nums[j] == target) return new int[]{i, j};
        return new int[0];
    }
}
```

## Tests
```java test=arrays/TwoSumTest.java
package arrays;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TwoSumTest {
    TwoSum s = new TwoSum();
    @Test void examples() {
        assertArrayEquals(new int[]{0, 1}, s.twoSum(new int[]{2, 7, 11, 15}, 9));
        assertArrayEquals(new int[]{1, 2}, s.twoSum(new int[]{3, 2, 4}, 6));
        assertArrayEquals(new int[]{0, 1}, s.twoSum(new int[]{3, 3}, 6));
    }
    @Test void negativesAndBrute() {
        assertArrayEquals(new int[]{0, 2}, s.twoSum(new int[]{-3, 4, 3, 90}, 0));
        assertArrayEquals(new int[]{1, 2}, s.twoSumBrute(new int[]{3, 2, 4}, 6));
    }
}
```
