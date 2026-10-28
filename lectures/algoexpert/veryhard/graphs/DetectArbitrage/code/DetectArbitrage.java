public class DetectArbitrage {
    public static boolean detectArbitrage(double[][] rates) {
        int n = rates.length;
        double[] dist = new double[n];
        java.util.Arrays.fill(dist, Double.MAX_VALUE);
        dist[0] = 0;
        for (int it = 0; it < n; it++) {
            boolean changed = false;
            for (int u = 0; u < n; u++) for (int v = 0; v < n; v++) {
                double w = -Math.log(rates[u][v]);
                if (dist[u] + w < dist[v] - 1e-12) { dist[v] = dist[u] + w; changed = true; }
            }
            if (!changed) return false;
        }
        return true;
    }
}
