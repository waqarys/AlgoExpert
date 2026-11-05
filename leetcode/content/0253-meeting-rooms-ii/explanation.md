# 0253. Meeting Rooms II

**Difficulty:** Medium | **Category:** Intervals | **LeetCode:** https://leetcode.com/problems/meeting-rooms-ii/

## Problem
- Return the minimum number of conference rooms required for all meetings.

## Intuition
- The answer is the maximum number of meetings in progress at any moment.
- Sweep line: sort starts and ends separately; walk through the starts, and whenever the earliest end is <= the current start, a room frees up.

## Brute Force
- For every time point count overlapping meetings: O(n * T).

## Optimal Approach
1. starts sorted, ends sorted; rooms = 0, e = 0.
2. For each start s: if s >= ends[e], e++ (reuse a room); else rooms++.

## Worked Example
- [[0,30],[5,10],[15,20]].
```text
starts 0 5 15 | ends 10 20 30
s=0  : 0 < 10   -> rooms 1
s=5  : 5 < 10   -> rooms 2
s=15 : 15 >= 10 -> reuse, e=1
answer 2
```

## Complexity
- Time: O(n log n). Space: O(n).

## Pitfalls
- A meeting ending at t frees the room for one starting at t (>=).
- A min-heap of end times is an equivalent and popular alternative.

## Video Script
- Draw meetings as bars; a vertical line sweeping across counts overlaps.

## Solution
```java file=intervals/MeetingRoomsII.java
package intervals;

import java.util.*;

/**
 * LC 253 Meeting Rooms II.
 * Approach: sweep sorted start and end times; reuse a room when the earliest end <= start.
 * Time O(n log n), Space O(n).
 */
public class MeetingRoomsII {
    public int minMeetingRooms(int[][] intervals) {
        int n = intervals.length;
        int[] starts = new int[n], ends = new int[n];
        for (int i = 0; i < n; i++) { starts[i] = intervals[i][0]; ends[i] = intervals[i][1]; }
        Arrays.sort(starts);
        Arrays.sort(ends);
        int rooms = 0, e = 0;
        for (int s : starts) {
            if (s >= ends[e]) e++;
            else rooms++;
        }
        return rooms;
    }
}
```

## Tests
```java test=intervals/MeetingRoomsIITest.java
package intervals;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MeetingRoomsIITest {
    MeetingRoomsII s = new MeetingRoomsII();
    @Test void examples() {
        assertEquals(2, s.minMeetingRooms(new int[][]{{0, 30}, {5, 10}, {15, 20}}));
        assertEquals(1, s.minMeetingRooms(new int[][]{{7, 10}, {2, 4}}));
        assertEquals(3, s.minMeetingRooms(new int[][]{{1, 5}, {2, 6}, {3, 7}}));
        assertEquals(0, s.minMeetingRooms(new int[][]{}));
    }
}
```
