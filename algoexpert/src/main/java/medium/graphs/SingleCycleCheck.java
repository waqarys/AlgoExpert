package medium.graphs;

/**
 * Single Cycle Check: each element is a jump (wrapping). Do the jumps form one cycle visiting every index
 * exactly once and returning to the start?
 * Time: O(n) | Space: O(1).
 */
public class SingleCycleCheck {
    public static boolean hasSingleCycle(int[] a) {
        int n = a.length, idx = 0;
        for (int visited = 0; visited < n; visited++) {
            if (visited > 0 && idx == 0) return false;
            idx = Math.floorMod(idx + a[idx], n);
        }
        return idx == 0;
    }
}
