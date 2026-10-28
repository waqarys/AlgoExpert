package hard.heaps;

import java.util.Collections;
import java.util.PriorityQueue;

/**
 * Continuous Median: insert numbers one at a time and query the running median, using a max-heap for the
 * lower half and a min-heap for the upper half.
 * Time: O(log n) insert, O(1) median | Space: O(n).
 */
public class ContinuousMedian {
    public static class ContinuousMedianHandler {
        private final PriorityQueue<Integer> lower = new PriorityQueue<>(Collections.reverseOrder());
        private final PriorityQueue<Integer> upper = new PriorityQueue<>();
        private double median;

        public void insert(int n) {
            if (lower.isEmpty() || n < lower.peek()) lower.add(n); else upper.add(n);
            if (lower.size() > upper.size() + 1) upper.add(lower.poll());
            else if (upper.size() > lower.size() + 1) lower.add(upper.poll());
            if (lower.size() == upper.size()) median = (lower.peek() + (double) upper.peek()) / 2;
            else median = lower.size() > upper.size() ? lower.peek() : upper.peek();
        }

        public double getMedian() { return median; }
    }
}
