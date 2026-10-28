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
