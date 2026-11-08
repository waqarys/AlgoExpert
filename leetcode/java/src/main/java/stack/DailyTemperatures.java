package stack;

import java.util.*;

/**
 * LC 739 Daily Temperatures.
 * Approach: monotonic decreasing stack of indices waiting for a warmer day.
 * Time O(n), Space O(n).
 */
public class DailyTemperatures {
    public int[] dailyTemperatures(int[] t) {
        int[] ans = new int[t.length];
        Deque<Integer> st = new ArrayDeque<>();
        for (int i = 0; i < t.length; i++) {
            while (!st.isEmpty() && t[i] > t[st.peek()]) {
                int j = st.pop();
                ans[j] = i - j;
            }
            st.push(i);
        }
        return ans;
    }
}
