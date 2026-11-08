# 0128. Longest Consecutive Sequence

**Difficulty:** Medium | **Category:** Arrays & Hashing | **LeetCode:** https://leetcode.com/problems/longest-consecutive-sequence/

## Problem
- Given an unsorted array, return the length of the longest run of consecutive integers (values, not positions), in O(n) time.
- Example: [100,4,200,1,3,2] -> 4 (the run 1,2,3,4).

## Intuition
- Put everything in a HashSet. A number x starts a run only if x-1 is not in the set.
- From each start, count upward x+1, x+2, ... while present.
- Each number is visited at most twice (once in the outer loop, once in some run), so the total is O(n).

## Brute Force
- Sort and scan for runs (skip duplicates): O(n log n).
- Or for every x count upwards without the "start" check: O(n^2) worst case.

## Optimal Approach
1. set = all values.
2. For each x in set: if !set.contains(x-1), walk y = x while set.contains(y+1), y++.
3. best = max(best, y - x + 1).

## Worked Example
- nums = [100, 4, 200, 1, 3, 2].
```text
x=100: 99 absent -> start, 101 absent -> len 1
x=4  : 3 present -> skip (not a start)
x=200: start -> len 1
x=1  : 0 absent -> start, 2,3,4 present, 5 absent -> len 4
x=3,2: not starts -> skip
best = 4
```

## Complexity
- Time: O(n) average.
- Space: O(n).

## Pitfalls
- Iterate over the set, not the array, so duplicates do not repeat runs (otherwise [1,1,1,...] style inputs can degrade).
- Empty input returns 0.

## Video Script
- "Sorting is the obvious answer, but the problem demands O(n)."
- Key insight: only count from sequence starts. Show why that makes the nested loop linear overall.

## Solution
```java file=arrays/LongestConsecutiveSequence.java
package arrays;

import java.util.*;

/**
 * LC 128 Longest Consecutive Sequence.
 * Approach: HashSet; only start counting at x where x-1 is absent, then extend upward.
 * Time O(n), Space O(n).
 */
public class LongestConsecutiveSequence {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int x : nums) set.add(x);
        int best = 0;
        for (int x : set) {
            if (set.contains(x - 1)) continue;
            int y = x;
            while (set.contains(y + 1)) y++;
            best = Math.max(best, y - x + 1);
        }
        return best;
    }
}
```

## Tests
```java test=arrays/LongestConsecutiveSequenceTest.java
package arrays;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LongestConsecutiveSequenceTest {
    LongestConsecutiveSequence s = new LongestConsecutiveSequence();
    @Test void examples() {
        assertEquals(4, s.longestConsecutive(new int[]{100, 4, 200, 1, 3, 2}));
        assertEquals(9, s.longestConsecutive(new int[]{0, 3, 7, 2, 5, 8, 4, 6, 0, 1}));
    }
    @Test void edges() {
        assertEquals(0, s.longestConsecutive(new int[]{}));
        assertEquals(3, s.longestConsecutive(new int[]{1, 2, 0, 1}));
        assertEquals(2, s.longestConsecutive(new int[]{Integer.MAX_VALUE, Integer.MAX_VALUE - 1}));
    }
}
```
