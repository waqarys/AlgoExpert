package heap;

import java.util.*;

/**
 * LC 703 Kth Largest Element in a Stream.
 * Approach: min-heap holding the k largest values; top is the answer.
 * add O(log k), Space O(k).
 */
public class KthLargest {
    private final PriorityQueue<Integer> heap = new PriorityQueue<>();
    private final int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        for (int x : nums) add(x);
    }

    public int add(int val) {
        heap.offer(val);
        if (heap.size() > k) heap.poll();
        return heap.peek();
    }
}
