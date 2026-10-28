package hard.arrays;

import java.util.HashSet;
import java.util.Set;

/**
 * Largest Range: [lo, hi] of the longest run of consecutive integers present in the array.
 * Time: O(n) | Space: O(n).
 */
public class LargestRange {
    public static int[] largestRange(int[] a) {
        Set<Integer> s = new HashSet<>();
        for (int x : a) s.add(x);
        int[] best = {a[0], a[0]};
        for (int x : s) {
            if (s.contains(x - 1)) continue;
            int y = x;
            while (s.contains(y + 1)) y++;
            if (y - x > best[1] - best[0]) best = new int[]{x, y};
        }
        return best;
    }
}
