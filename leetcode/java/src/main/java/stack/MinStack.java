package stack;

import java.util.*;

/**
 * LC 155 Min Stack.
 * Approach: each entry stores {value, min of the stack up to this entry}.
 * Time O(1) per op, Space O(n).
 */
public class MinStack {
    private final Deque<int[]> st = new ArrayDeque<>();

    public void push(int val) {
        int min = st.isEmpty() ? val : Math.min(val, st.peek()[1]);
        st.push(new int[]{val, min});
    }

    public void pop() { st.pop(); }

    public int top() { return st.peek()[0]; }

    public int getMin() { return st.peek()[1]; }
}
