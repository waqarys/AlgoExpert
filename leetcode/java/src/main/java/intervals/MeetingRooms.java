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
