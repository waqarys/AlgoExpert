package hard.arrays;

import java.util.ArrayList;
import java.util.List;

/**
 * Zigzag Traverse: read a matrix along anti-diagonals in zigzag, starting at top-left and moving down first
 * (odd diagonals are read bottom-to-top, even ones top-to-bottom).
 * Time: O(n) | Space: O(n).
 */
public class ZigzagTraverse {
    public static List<Integer> zigzagTraverse(List<List<Integer>> m) {
        List<Integer> out = new ArrayList<>();
        int R = m.size(), C = m.get(0).size();
        for (int d = 0; d < R + C - 1; d++) {
            int lo = Math.max(0, d - C + 1), hi = Math.min(d, R - 1);
            if (d % 2 == 0) for (int r = lo; r <= hi; r++) out.add(m.get(r).get(d - r));
            else for (int r = hi; r >= lo; r--) out.add(m.get(r).get(d - r));
        }
        return out;
    }
}
