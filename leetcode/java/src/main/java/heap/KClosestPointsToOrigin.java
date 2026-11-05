package heap;

import java.util.*;

/**
 * LC 973 K Closest Points to Origin.
 * Approach: max-heap of size k keyed by squared distance.
 * Time O(n log k), Space O(k).
 */
public class KClosestPointsToOrigin {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Long.compare(dist(b), dist(a)));
        for (int[] p : points) {
            pq.offer(p);
            if (pq.size() > k) pq.poll();
        }
        return pq.toArray(new int[0][]);
    }

    private static long dist(int[] p) { return (long) p[0] * p[0] + (long) p[1] * p[1]; }
}
