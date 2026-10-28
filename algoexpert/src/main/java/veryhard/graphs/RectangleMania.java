package veryhard.graphs;

import java.util.HashSet;
import java.util.Set;

/**
 * Rectangle Mania: count axis-aligned rectangles whose four corners are all in the point set.
 * Each pair forming a strictly up-right diagonal identifies one rectangle exactly once.
 * Time: O(n^2) | Space: O(n).
 */
public class RectangleMania {
    public static int rectangleMania(int[][] coords) {
        Set<String> set = new HashSet<>();
        for (int[] p : coords) set.add(p[0] + "," + p[1]);
        int count = 0;
        for (int[] a : coords) for (int[] b : coords)
            if (b[0] > a[0] && b[1] > a[1] && set.contains(a[0] + "," + b[1]) && set.contains(b[0] + "," + a[1])) count++;
        return count;
    }
}
