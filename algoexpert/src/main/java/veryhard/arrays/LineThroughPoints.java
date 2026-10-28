package veryhard.arrays;

import java.util.HashMap;
import java.util.Map;

/**
 * Line Through Points: maximum number of the given (unique, integer) points lying on one straight line.
 * For each anchor, count normalised slopes (reduced by gcd, sign-canonicalised).
 * Time: O(n^2) | Space: O(n).
 */
public class LineThroughPoints {
    public static int lineThroughPoints(int[][] points) {
        int best = Math.min(points.length, 1);
        for (int i = 0; i < points.length; i++) {
            Map<String, Integer> slopes = new HashMap<>();
            for (int j = i + 1; j < points.length; j++) {
                int dx = points[j][0] - points[i][0], dy = points[j][1] - points[i][1];
                int g = gcd(Math.abs(dx), Math.abs(dy));
                dx /= g; dy /= g;
                if (dx < 0 || (dx == 0 && dy < 0)) { dx = -dx; dy = -dy; }
                best = Math.max(best, slopes.merge(dx + "/" + dy, 1, Integer::sum) + 1);
            }
        }
        return best;
    }

    private static int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
}
