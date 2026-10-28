package hard.heaps;

import java.util.PriorityQueue;

/**
 * Sort K-Sorted Array: every element is at most k positions from its sorted position; sort with a size-(k+1)
 * min-heap.
 * Time: O(n log k) | Space: O(k).
 */
public class SortKSortedArray {
    public static int[] sortKSortedArray(int[] a, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int w = 0;
        for (int i = 0; i < a.length; i++) {
            pq.add(a[i]);
            if (pq.size() > k) a[w++] = pq.poll();
        }
        while (!pq.isEmpty()) a[w++] = pq.poll();
        return a;
    }
}
