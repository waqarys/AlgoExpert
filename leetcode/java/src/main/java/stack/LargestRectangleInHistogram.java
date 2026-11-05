package stack;

import java.util.*;

/**
 * LC 84 Largest Rectangle in Histogram.
 * Approach: monotonic increasing stack; a popped bar's rectangle spans (new top, i) exclusive.
 * Time O(n), Space O(n).
 */
public class LargestRectangleInHistogram {
    public int largestRectangleArea(int[] h) {
        Deque<Integer> st = new ArrayDeque<>();
        int best = 0, n = h.length;
        for (int i = 0; i <= n; i++) {
            int cur = i == n ? 0 : h[i];
            while (!st.isEmpty() && cur < h[st.peek()]) {
                int height = h[st.pop()];
                int left = st.isEmpty() ? -1 : st.peek();
                best = Math.max(best, height * (i - left - 1));
            }
            st.push(i);
        }
        return best;
    }
}
