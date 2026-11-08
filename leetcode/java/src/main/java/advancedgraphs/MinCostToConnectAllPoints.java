package advancedgraphs;

import java.util.*;

/**
 * LC 1584 Min Cost to Connect All Points.
 * Approach: dense Prim's MST with an O(n) scan for the next closest point.
 * Time O(n^2), Space O(n).
 */
public class MinCostToConnectAllPoints {
    public int minCostConnectPoints(int[][] pts) {
        int n = pts.length, cost = 0;
        int[] dist = new int[n];
        boolean[] in = new boolean[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[0] = 0;
        for (int iter = 0; iter < n; iter++) {
            int u = -1;
            for (int v = 0; v < n; v++) if (!in[v] && (u == -1 || dist[v] < dist[u])) u = v;
            in[u] = true;
            cost += dist[u];
            for (int v = 0; v < n; v++) {
                if (in[v]) continue;
                int d = Math.abs(pts[u][0] - pts[v][0]) + Math.abs(pts[u][1] - pts[v][1]);
                if (d < dist[v]) dist[v] = d;
            }
        }
        return cost;
    }
}
