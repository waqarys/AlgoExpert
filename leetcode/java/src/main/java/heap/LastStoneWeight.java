package heap;

import java.util.*;

/**
 * LC 1046 Last Stone Weight.
 * Approach: max-heap simulation.
 * Time O(n log n), Space O(n).
 */
public class LastStoneWeight {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int s : stones) pq.add(s);
        while (pq.size() > 1) {
            int y = pq.poll(), x = pq.poll();
            if (y != x) pq.add(y - x);
        }
        return pq.isEmpty() ? 0 : pq.peek();
    }
}
