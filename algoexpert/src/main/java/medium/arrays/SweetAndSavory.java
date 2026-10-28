package medium.arrays;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Sweet And Savory: dishes have negative (sweet) or positive (savory) flavour. Pick one sweet + one savory
 * whose sum is closest to target without exceeding it; return [sweet, savory] or [0, 0].
 * Time: O(n log n) | Space: O(n).
 */
public class SweetAndSavory {
    public static int[] sweetAndSavory(int[] dishes, int target) {
        List<Integer> sweet = new ArrayList<>(), savory = new ArrayList<>();
        for (int d : dishes) if (d < 0) sweet.add(d); else if (d > 0) savory.add(d);
        sweet.sort(Collections.reverseOrder());
        Collections.sort(savory);
        int[] best = {0, 0};
        long bestDiff = Long.MAX_VALUE;
        int i = 0, j = 0;
        while (i < sweet.size() && j < savory.size()) {
            long sum = (long) sweet.get(i) + savory.get(j);
            if (sum <= target) {
                if (target - sum < bestDiff) { bestDiff = target - sum; best = new int[]{sweet.get(i), savory.get(j)}; }
                j++;
            } else i++;
        }
        return best;
    }
}
