package stack;

import java.util.*;

/**
 * LC 20 Valid Parentheses.
 * Approach: stack of expected closers; each closer must match the top.
 * Time O(n), Space O(n).
 */
public class ValidParentheses {
    public boolean isValid(String s) {
        Deque<Character> st = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (c == '(') st.push(')');
            else if (c == '[') st.push(']');
            else if (c == '{') st.push('}');
            else if (st.isEmpty() || st.pop() != c) return false;
        }
        return st.isEmpty();
    }
}
