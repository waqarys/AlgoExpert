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
