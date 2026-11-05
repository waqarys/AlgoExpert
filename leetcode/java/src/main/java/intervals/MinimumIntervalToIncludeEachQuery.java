package intervals;

import java.util.*;

/**
 * LC 1851 Minimum Interval to Include Each Query.
 * Approach: offline sorted queries + min-heap of (size, right); evict intervals ending before q.
 * Time O((n+q) log n + q log q), Space O(n+q).
 */
public class MinimumIntervalToIncludeEachQuery {
    public int[] minInterval(int[][] intervals, int[] queries) {
        int[][] iv = intervals.clone();
        Arrays.sort(iv, (a, b) -> Integer.compare(a[0], b[0]));
        Integer[] order = new Integer[queries.length];
        for (int i = 0; i < order.length; i++) order[i] = i;
        Arrays.sort(order, (a, b) -> Integer.compare(queries[a], queries[b]));
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0])); // {size, right}
        int[] ans = new int[queries.length];
        int i = 0;
        for (int qi : order) {
            int q = queries[qi];
            while (i < iv.length && iv[i][0] <= q) { pq.add(new int[]{iv[i][1] - iv[i][0] + 1, iv[i][1]}); i++; }
            while (!pq.isEmpty() && pq.peek()[1] < q) pq.poll();
            ans[qi] = pq.isEmpty() ? -1 : pq.peek()[0];
        }
        return ans;
    }
}
