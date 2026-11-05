package graphs;

/**
 * LC 323 Number of Connected Components in an Undirected Graph.
 * Approach: Union-Find; each successful union reduces the component count.
 * Time O(E * alpha(n)), Space O(n).
 */
public class NumberOfConnectedComponents {
    public int countComponents(int n, int[][] edges) {
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int comps = n;
        for (int[] e : edges) {
            int a = find(parent, e[0]), b = find(parent, e[1]);
            if (a != b) { parent[a] = b; comps--; }
        }
        return comps;
    }

    private int find(int[] p, int x) {
        while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; }
        return x;
    }
}
