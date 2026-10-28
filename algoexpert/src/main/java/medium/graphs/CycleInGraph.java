package medium.graphs;

/**
 * Cycle In Graph: directed graph as adjacency list; does it contain a cycle? 3-colour DFS.
 * Time: O(v + e) | Space: O(v).
 */
public class CycleInGraph {
    public static boolean cycleInGraph(int[][] edges) {
        int[] color = new int[edges.length];
        for (int v = 0; v < edges.length; v++) if (color[v] == 0 && dfs(v, edges, color)) return true;
        return false;
    }

    private static boolean dfs(int v, int[][] edges, int[] color) {
        color[v] = 1;
        for (int w : edges[v]) {
            if (color[w] == 1) return true;
            if (color[w] == 0 && dfs(w, edges, color)) return true;
        }
        color[v] = 2;
        return false;
    }
}
