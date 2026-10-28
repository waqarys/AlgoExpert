package medium.stacks;

import java.util.ArrayDeque;

/**
 * Balanced Brackets: are (), [], {} properly balanced and nested? Non-bracket chars are ignored.
 * Time: O(n) | Space: O(n).
 */
public class BalancedBrackets {
    public static boolean balancedBrackets(String s) {
        ArrayDeque<Character> st = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if ("([{".indexOf(c) >= 0) st.push(c);
            else if (")]}".indexOf(c) >= 0) {
                if (st.isEmpty() || "([{".indexOf(st.pop()) != ")]}".indexOf(c)) return false;
            }
        }
        return st.isEmpty();
    }
}
