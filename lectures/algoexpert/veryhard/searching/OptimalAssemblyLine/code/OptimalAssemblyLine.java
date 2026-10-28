public class OptimalAssemblyLine {
    public static int optimalAssemblyLine(int[] steps, int k) {
        int lo = 0, hi = 0;
        for (int s : steps) { lo = Math.max(lo, s); hi += s; }
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (stations(steps, mid) <= k) hi = mid; else lo = mid + 1;
        }
        return lo;
    }

    private static int stations(int[] steps, int cap) {
        int count = 1, cur = 0;
        for (int s : steps) { if (cur + s > cap) { count++; cur = 0; } cur += s; }
        return count;
    }
}
