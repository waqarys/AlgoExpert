# 0056. Merge Intervals

**Difficulty:** Medium | **Category:** Intervals | **LeetCode:** https://leetcode.com/problems/merge-intervals/

## Problem
- Merge all overlapping intervals.

## Intuition
- After sorting by start, overlapping intervals are adjacent. Extend the last merged interval while the next one starts before it ends.

## Brute Force
- Compare every pair repeatedly until nothing merges: O(n^2) or worse.

## Optimal Approach
1. Sort by start.
2. For each interval: if it starts <= last.end, last.end = max(last.end, end); else append it.

## Worked Example
- [[1,3],[2,6],[8,10],[15,18]].
```text
[1,3]   -> res [[1,3]]
[2,6]   2 <= 3 -> [1,6]
[8,10]  new
[15,18] new
result [[1,6],[8,10],[15,18]]
```

## Complexity
- Time: O(n log n). Space: O(n).

## Pitfalls
- Use max for the end: [1,10] then [2,3] must stay [1,10].

## Video Script
- The interval template: sort, then sweep.

## Solution
```java file=intervals/MergeIntervals.java
package intervals;

import java.util.*;

/**
 * LC 56 Merge Intervals.
 * Approach: sort by start, sweep and extend the last merged interval.
 * Time O(n log n), Space O(n).
 */
public class MergeIntervals {
    public int[][] merge(int[][] intervals) {
        int[][] a = intervals.clone();
        Arrays.sort(a, (x, y) -> Integer.compare(x[0], y[0]));
        List<int[]> res = new ArrayList<>();
        for (int[] cur : a) {
            if (!res.isEmpty() && cur[0] <= res.get(res.size() - 1)[1]) {
                int[] last = res.get(res.size() - 1);
                last[1] = Math.max(last[1], cur[1]);
            } else {
                res.add(new int[]{cur[0], cur[1]});
            }
        }
        return res.toArray(new int[0][]);
    }
}
```

## Tests
```java test=intervals/MergeIntervalsTest.java
package intervals;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MergeIntervalsTest {
    MergeIntervals s = new MergeIntervals();
    @Test void examples() {
        assertArrayEquals(new int[][]{{1, 6}, {8, 10}, {15, 18}}, s.merge(new int[][]{{1, 3}, {2, 6}, {8, 10}, {15, 18}}));
        assertArrayEquals(new int[][]{{1, 5}}, s.merge(new int[][]{{1, 4}, {4, 5}}));
        assertArrayEquals(new int[][]{{1, 10}}, s.merge(new int[][]{{2, 3}, {1, 10}}));
    }
}
```
