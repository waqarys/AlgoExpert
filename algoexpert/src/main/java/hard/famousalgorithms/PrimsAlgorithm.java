package hard.famousalgorithms;

import java.util.*;

/**
 * Prim's Algorithm: minimum spanning tree of a connected undirected weighted graph (adjacency list of
 * [dest, weight]), grown from vertex 0 with a min-heap of frontier edges.
 * Time: O(e log v) | Space: O(v + e).
 */
public class PrimsAlgorithm {
    public static int[][][] primsAlgorithm(int[][][] edges) {
        int n = edges.length;
        boolean[] in = new boolean[n];
        List<List<int[]>> mst = new ArrayList<>();
        for (int i = 0; i < n; i++) mst.add(new ArrayList<>());
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(e -> e[2]));
        in[0] = true;
        for (int[] e : edges[0]) pq.add(new int[]{0, e[0], e[1]});
        while (!pq.isEmpty()) {
            int[] e = pq.poll();
            if (in[e[1]]) continue;
            in[e[1]] = true;
            mst.get(e[0]).add(new int[]{e[1], e[2]});
            mst.get(e[1]).add(new int[]{e[0], e[2]});
            for (int[] f : edges[e[1]]) if (!in[f[0]]) pq.add(new int[]{e[1], f[0], f[1]});
        }
        int[][][] out = new int[n][][];
        for (int i = 0; i < n; i++) out[i] = mst.get(i).toArray(new int[0][]);
        return out;
    }
}
