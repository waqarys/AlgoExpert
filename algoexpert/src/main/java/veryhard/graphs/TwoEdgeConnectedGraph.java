package veryhard.graphs;

/**
 * Two-Edge-Connected Graph: undirected adjacency list; is the graph connected and free of bridges (stays
 * connected after removing any single edge)? Empty graph counts as true. Tarjan low-link.
 * Time: O(v + e) | Space: O(v).
 */
public class TwoEdgeConnectedGraph {
    public static boolean twoEdgeConnectedGraph(int[][] edges) {
        int n = edges.length;
        if (n == 0) return true;
        int[] disc = new int[n], low = new int[n];
        java.util.Arrays.fill(disc, -1);
        int[] time = {0};
        if (hasBridge(0, -1, edges, disc, low, time)) return false;
        for (int d : disc) if (d == -1) return false;
        return true;
    }

    private static boolean hasBridge(int v, int parent, int[][] edges, int[] disc, int[] low, int[] time) {
        disc[v] = low[v] = time[0]++;
        boolean skippedParent = false;
        for (int w : edges[v]) {
            if (w == parent && !skippedParent) { skippedParent = true; continue; }
            if (disc[w] == -1) {
                if (hasBridge(w, v, edges, disc, low, time)) return true;
                low[v] = Math.min(low[v], low[w]);
                if (low[w] > disc[v]) return true;
            } else low[v] = Math.min(low[v], disc[w]);
        }
        return false;
    }
}
