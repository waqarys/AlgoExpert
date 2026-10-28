package medium.stacks;

import java.util.ArrayList;

/**
 * Sort Stack: sort a stack (list, top = end) ascending using only push/pop/peek and recursion.
 * Time: O(n^2) | Space: O(n) recursion.
 */
public class SortStack {
    public static ArrayList<Integer> sortStack(ArrayList<Integer> stack) {
        if (stack.isEmpty()) return stack;
        int top = stack.remove(stack.size() - 1);
        sortStack(stack);
        insert(stack, top);
        return stack;
    }

    private static void insert(ArrayList<Integer> st, int v) {
        if (st.isEmpty() || st.get(st.size() - 1) <= v) { st.add(v); return; }
        int top = st.remove(st.size() - 1);
        insert(st, v);
        st.add(top);
    }
}
