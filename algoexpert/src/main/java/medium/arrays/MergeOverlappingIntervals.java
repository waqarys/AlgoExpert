package medium.arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Merge Overlapping Intervals: merge all overlapping [start, end] intervals; result sorted by start.
 * Time: O(n log n) | Space: O(n).
 */
public class MergeOverlappingIntervals {
    public static int[][] mergeOverlappingIntervals(int[][] intervals) {
        int[][] s = intervals.clone();
        Arrays.sort(s, (x, y) -> Integer.compare(x[0], y[0]));
        List<int[]> out = new ArrayList<>();
        for (int[] iv : s) {
            if (!out.isEmpty() && out.get(out.size() - 1)[1] >= iv[0])
                out.get(out.size() - 1)[1] = Math.max(out.get(out.size() - 1)[1], iv[1]);
            else out.add(new int[]{iv[0], iv[1]});
        }
        return out.toArray(new int[0][]);
    }
}
