# 0252. Meeting Rooms

**Difficulty:** Easy | **Category:** Intervals | **LeetCode:** https://leetcode.com/problems/meeting-rooms/

## Problem
- Given meeting time intervals, can one person attend all of them?

## Intuition
- Sort by start; any meeting that starts before the previous one ends is a conflict.

## Brute Force
- Compare all pairs: O(n^2).

## Optimal Approach
1. Sort by start.
2. For i >= 1: if a[i].start < a[i-1].end return false.

## Worked Example
- [[0,30],[5,10],[15,20]].
```text
sorted: [0,30] [5,10] [15,20]
5 < 30 -> conflict -> false
```

## Complexity
- Time: O(n log n). Space: O(1).

## Pitfalls
- [5,10] and [10,15] do not conflict (strict <).

## Video Script
- Warm-up for Meeting Rooms II.

## Solution
```java file=intervals/MeetingRooms.java
package intervals;

import java.util.*;

/**
 * LC 252 Meeting Rooms.
 * Approach: sort by start and check adjacent overlaps.
 * Time O(n log n), Space O(1).
 */
public class MeetingRooms {
    public boolean canAttendMeetings(int[][] intervals) {
        int[][] a = intervals.clone();
        Arrays.sort(a, (x, y) -> Integer.compare(x[0], y[0]));
        for (int i = 1; i < a.length; i++) if (a[i][0] < a[i - 1][1]) return false;
        return true;
    }
}
```

## Tests
```java test=intervals/MeetingRoomsTest.java
package intervals;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MeetingRoomsTest {
    MeetingRooms s = new MeetingRooms();
    @Test void examples() {
        assertFalse(s.canAttendMeetings(new int[][]{{0, 30}, {5, 10}, {15, 20}}));
        assertTrue(s.canAttendMeetings(new int[][]{{7, 10}, {2, 4}}));
        assertTrue(s.canAttendMeetings(new int[][]{{5, 10}, {10, 15}}));
        assertTrue(s.canAttendMeetings(new int[][]{}));
    }
}
```
