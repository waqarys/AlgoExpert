package math;

import java.util.*;

/**
 * LC 2013 Detect Squares.
 * Approach: point counts in a hash map; for each diagonal candidate multiply the other corners' counts.
 * add O(1), count O(distinct points).
 */
public class DetectSquares {
    private final Map<Long, Integer> cnt = new HashMap<>();
    private final List<int[]> distinct = new ArrayList<>();

    private static long key(int x, int y) { return ((long) x << 32) | (y & 0xffffffffL); }

    public void add(int[] p) {
        if (cnt.merge(key(p[0], p[1]), 1, Integer::sum) == 1) distinct.add(p);
    }

    public int count(int[] q) {
        int qx = q[0], qy = q[1], total = 0;
        for (int[] p : distinct) {
            int x = p[0], y = p[1];
            if (Math.abs(x - qx) != Math.abs(y - qy) || x == qx) continue;
            total += cnt.get(key(x, y)) * cnt.getOrDefault(key(qx, y), 0) * cnt.getOrDefault(key(x, qy), 0);
        }
        return total;
    }
}
