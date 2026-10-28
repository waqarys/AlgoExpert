package veryhard.heaps;

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

/**
 * Merge Sorted Arrays: merge k sorted lists into one sorted list using a min-heap of (value, list, index).
 * Time: O(n log k) | Space: O(n + k).
 */
public class MergeSortedArrays {
    public static List<Integer> mergeSortedArrays(List<List<Integer>> arrays) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        for (int i = 0; i < arrays.size(); i++) if (!arrays.get(i).isEmpty()) pq.add(new int[]{arrays.get(i).get(0), i, 0});
        List<Integer> out = new ArrayList<>();
        while (!pq.isEmpty()) {
            int[] t = pq.poll();
            out.add(t[0]);
            List<Integer> src = arrays.get(t[1]);
            if (t[2] + 1 < src.size()) pq.add(new int[]{src.get(t[2] + 1), t[1], t[2] + 1});
        }
        return out;
    }
}
