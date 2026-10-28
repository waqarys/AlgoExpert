package veryhard.graphs;

/**
 * Detect Arbitrage: exchange-rate matrix; is there a cycle of trades yielding profit? Take -log(rate)
 * edge weights and look for a negative cycle with Bellman-Ford.
 * Time: O(n^3) | Space: O(n^2).
 */
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
