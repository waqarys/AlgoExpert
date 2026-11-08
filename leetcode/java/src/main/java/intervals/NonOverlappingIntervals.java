package intervals;

import java.util.*;

/**
 * LC 435 Non-overlapping Intervals.
 * Approach: sort by end; keep earliest-finishing compatible intervals, count the rest.
 * Time O(n log n), Space O(1).
 */
public class NonOverlappingIntervals {
    public int eraseOverlapIntervals(int[][] intervals) {
        int[][] a = intervals.clone();
        Arrays.sort(a, (x, y) -> Integer.compare(x[1], y[1]));
        int removed = 0;
        long prevEnd = Long.MIN_VALUE;
        for (int[] in : a) {
            if (in[0] >= prevEnd) prevEnd = in[1];
            else removed++;
        }
        return removed;
    }
}
