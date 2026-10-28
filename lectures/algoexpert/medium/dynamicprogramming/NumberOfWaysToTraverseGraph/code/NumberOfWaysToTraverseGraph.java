public class NumberOfWaysToTraverseGraph {
    public static long numberOfWaysToTraverseGraph(int width, int height) {
        int n = width + height - 2, k = Math.min(width, height) - 1;
        long r = 1;
        for (int i = 1; i <= k; i++) r = r * (n - k + i) / i;
        return r;
    }
}
