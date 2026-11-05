# 0217. Contains Duplicate

**Difficulty:** Easy | **Category:** Arrays & Hashing | **LeetCode:** https://leetcode.com/problems/contains-duplicate/

## Problem
- Given an integer array nums, return true if any value appears at least twice, otherwise false.
- Example: [1,2,3,1] -> true, [1,2,3,4] -> false.

## Intuition
- We only need to know "have I seen this value before?" while scanning once.
- A HashSet answers that membership question in O(1) average time.

## Brute Force
- Compare every pair (i, j) with i < j: O(n^2) time, O(1) space.
- Sorting first and checking neighbours is O(n log n) time and modifies the input.

## Optimal Approach
1. Create an empty HashSet.
2. For each number: if set.add(x) returns false, x was already present, so return true.
3. If the loop ends, every value was unique, so return false.

## Worked Example
- Input nums = [1, 2, 3, 1].
```text
x=1  set={}        -> add -> {1}
x=2  set={1}       -> add -> {1,2}
x=3  set={1,2}     -> add -> {1,2,3}
x=1  set={1,2,3}   -> add fails -> return true
```

## Complexity
- Time: O(n) average, one pass with O(1) set operations.
- Space: O(n) for the set in the worst case (all unique).

## Pitfalls
- Use the boolean return of Set.add instead of contains + add (one hash lookup instead of two).
- Empty and single-element arrays are trivially false.

## Video Script
- Hook: "The easiest hashing problem, but it teaches the pattern behind half of all array problems."
- Show the O(n^2) pair check, then ask: what do we repeat? Looking back at earlier values.
- Introduce the set as memory of the past, walk the trace, and finish with complexity and the sorting trade-off.

## Solution
```java file=arrays/ContainsDuplicate.java
package arrays;

import java.util.*;

/**
 * LC 217 Contains Duplicate. Return true if any value repeats.
 * Approach: single pass with a HashSet; add() returns false on a repeat.
 * Time O(n), Space O(n).
 */
public class ContainsDuplicate {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int x : nums) {
            if (!seen.add(x)) return true;
        }
        return false;
    }

    /** Teaching baseline: sort and compare neighbours. O(n log n) time. */
    public boolean containsDuplicateSort(int[] nums) {
        int[] a = nums.clone();
        Arrays.sort(a);
        for (int i = 1; i < a.length; i++) if (a[i] == a[i - 1]) return true;
        return false;
    }
}
```

## Tests
```java test=arrays/ContainsDuplicateTest.java
package arrays;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ContainsDuplicateTest {
    ContainsDuplicate s = new ContainsDuplicate();
    @Test void examples() {
        assertTrue(s.containsDuplicate(new int[]{1, 2, 3, 1}));
        assertFalse(s.containsDuplicate(new int[]{1, 2, 3, 4}));
        assertTrue(s.containsDuplicate(new int[]{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}));
    }
    @Test void edges() {
        assertFalse(s.containsDuplicate(new int[]{}));
        assertFalse(s.containsDuplicate(new int[]{7}));
        assertTrue(s.containsDuplicateSort(new int[]{-1, 5, -1}));
    }
}
```
