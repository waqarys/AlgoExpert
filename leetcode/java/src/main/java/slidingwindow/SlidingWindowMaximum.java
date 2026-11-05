package slidingwindow;

import java.util.*;

/**
 * LC 239 Sliding Window Maximum.
 * Approach: monotonic decreasing deque of indices; front is the window max.
 * Time O(n), Space O(k).
 */
public class SlidingWindowMaximum {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] out = new int[nums.length - k + 1];
        Deque<Integer> dq = new ArrayDeque<>();
        for (int i = 0; i < nums.length; i++) {
            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) dq.pollLast();
            dq.offerLast(i);
            if (dq.peekFirst() <= i - k) dq.pollFirst();
            if (i >= k - 1) out[i - k + 1] = nums[dq.peekFirst()];
        }
        return out;
    }
}
