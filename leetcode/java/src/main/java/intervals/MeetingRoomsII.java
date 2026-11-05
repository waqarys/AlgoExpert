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
