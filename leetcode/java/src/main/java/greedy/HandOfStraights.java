package greedy;

import java.util.*;

/**
 * LC 846 Hand of Straights.
 * Approach: TreeMap counts; the smallest remaining card always starts a group.
 * Time O(n log n), Space O(n).
 */
public class HandOfStraights {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        if (hand.length % groupSize != 0) return false;
        TreeMap<Integer, Integer> count = new TreeMap<>();
        for (int c : hand) count.merge(c, 1, Integer::sum);
        while (!count.isEmpty()) {
            int x = count.firstKey();
            for (int v = x; v < x + groupSize; v++) {
                Integer c = count.get(v);
                if (c == null) return false;
                if (c == 1) count.remove(v);
                else count.put(v, c - 1);
            }
        }
        return true;
    }
}
