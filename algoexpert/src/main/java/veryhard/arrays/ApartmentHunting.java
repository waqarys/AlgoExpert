package veryhard.arrays;

import java.util.List;
import java.util.Map;

/**
 * Apartment Hunting: blocks list which buildings (reqs) they contain. Choose the block minimising the
 * farthest distance you'd walk to reach any required building. Precompute nearest distance per req with
 * a left and right sweep.
 * Time: O(b*r) | Space: O(b*r).
 */
public class ApartmentHunting {
    public static int apartmentHunting(List<Map<String, Boolean>> blocks, String[] reqs) {
        int n = blocks.size();
        int[] worst = new int[n];
        for (String r : reqs) {
            int[] d = new int[n];
            int last = -1_000_000;
            for (int i = 0; i < n; i++) { if (blocks.get(i).getOrDefault(r, false)) last = i; d[i] = i - last; }
            last = 2_000_000;
            for (int i = n - 1; i >= 0; i--) { if (blocks.get(i).getOrDefault(r, false)) last = i; d[i] = Math.min(d[i], last - i); }
            for (int i = 0; i < n; i++) worst[i] = Math.max(worst[i], d[i]);
        }
        int best = 0;
        for (int i = 1; i < n; i++) if (worst[i] < worst[best]) best = i;
        return best;
    }
}
