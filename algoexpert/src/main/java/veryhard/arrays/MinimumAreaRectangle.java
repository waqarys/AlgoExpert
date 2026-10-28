package veryhard.arrays;

import java.util.HashSet;
import java.util.Set;

/**
 * Minimum Area Rectangle: smallest-area axis-aligned rectangle whose 4 corners are in the point set, else 0.
 * Treat each pair as a diagonal and check the other two corners.
 * Time: O(n^2) | Space: O(n).
 */
public class MinimumAreaRectangle {
    public static int minimumAreaRectangle(int[][] points) {
        Set<Long> set = new HashSet<>();
        for (int[] p : points) set.add(key(p[0], p[1]));
        long best = Long.MAX_VALUE;
        for (int i = 0; i < points.length; i++)
            for (int j = i + 1; j < points.length; j++) {
                int[] a = points[i], b = points[j];
                if (a[0] == b[0] || a[1] == b[1]) continue;
                if (set.contains(key(a[0], b[1])) && set.contains(key(b[0], a[1])))
                    best = Math.min(best, (long) Math.abs(a[0] - b[0]) * Math.abs(a[1] - b[1]));
            }
        return best == Long.MAX_VALUE ? 0 : (int) best;
    }

    private static long key(int x, int y) { return ((long) x << 32) ^ (y & 0xffffffffL); }
}
