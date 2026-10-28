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
