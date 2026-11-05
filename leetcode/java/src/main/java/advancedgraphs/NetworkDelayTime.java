package advancedgraphs;

import java.util.*;

/**
 * LC 743 Network Delay Time.
 * Approach: Dijkstra with a lazy min-heap; answer = max shortest distance.
 * Time O(E log V), Space O(V+E).
 */
public class NetworkDelayTime {
    public int networkDelayTime(int[][] times, int n, int k) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());
        for (int[] t : times) adj.get(t[0]).add(new int[]{t[1], t[2]});
        int[] dist = new int[n + 1];
        Arrays.fill(dist, -1);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        pq.add(new int[]{0, k});
        int done = 0, max = 0;
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int d = cur[0], u = cur[1];
            if (dist[u] != -1) continue;
            dist[u] = d;
            done++;
            max = Math.max(max, d);
            for (int[] e : adj.get(u)) if (dist[e[0]] == -1) pq.add(new int[]{d + e[1], e[0]});
        }
        return done == n ? max : -1;
    }
}
