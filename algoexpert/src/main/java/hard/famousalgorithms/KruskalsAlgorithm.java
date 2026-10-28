package hard.famousalgorithms;

import java.util.*;

/**
 * Kruskal's Algorithm: undirected weighted graph as adjacency list ([dest, weight]); return its minimum
 * spanning tree (forest) in the same format. Sort edges + union-find.
 * Time: O(e log e) | Space: O(v + e).
 */
public class KruskalsAlgorithm {
    public static int[][][] kruskalsAlgorithm(int[][][] edges) {
        int n = edges.length;
        List<int[]> all = new ArrayList<>();
        for (int u = 0; u < n; u++) for (int[] e : edges[u]) if (u < e[0]) all.add(new int[]{u, e[0], e[1]});
        all.sort(Comparator.comparingInt(e -> e[2]));
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        List<List<int[]>> mst = new ArrayList<>();
        for (int i = 0; i < n; i++) mst.add(new ArrayList<>());
        for (int[] e : all) {
            int a = find(parent, e[0]), b = find(parent, e[1]);
            if (a == b) continue;
            parent[a] = b;
            mst.get(e[0]).add(new int[]{e[1], e[2]});
            mst.get(e[1]).add(new int[]{e[0], e[2]});
        }
        int[][][] out = new int[n][][];
        for (int i = 0; i < n; i++) out[i] = mst.get(i).toArray(new int[0][]);
        return out;
    }

    private static int find(int[] p, int x) { while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; } return x; }
}
