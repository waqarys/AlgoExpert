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
