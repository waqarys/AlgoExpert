package intervals;

import java.util.*;

/**
 * LC 57 Insert Interval.
 * Approach: copy left intervals, merge overlapping ones into newInterval, copy the rest.
 * Time O(n), Space O(n).
 */
public class InsertInterval {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> res = new ArrayList<>();
        int i = 0, n = intervals.length;
        int start = newInterval[0], end = newInterval[1];
        while (i < n && intervals[i][1] < start) res.add(intervals[i++]);
        while (i < n && intervals[i][0] <= end) {
            start = Math.min(start, intervals[i][0]);
            end = Math.max(end, intervals[i][1]);
            i++;
        }
        res.add(new int[]{start, end});
        while (i < n) res.add(intervals[i++]);
        return res.toArray(new int[0][]);
    }
}
