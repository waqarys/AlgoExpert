package medium.stacks;

import java.util.ArrayDeque;

/**
 * Best Digits: remove exactly numDigits digits from a number string to make the largest possible number.
 * Monotonic decreasing stack.
 * Time: O(n) | Space: O(n).
 */
public class BestDigits {
    public static String bestDigits(String number, int numDigits) {
        ArrayDeque<Character> st = new ArrayDeque<>();
        int k = numDigits;
        for (char c : number.toCharArray()) {
            while (k > 0 && !st.isEmpty() && st.peekLast() < c) { st.pollLast(); k--; }
            st.addLast(c);
        }
        while (k-- > 0) st.pollLast();
        StringBuilder sb = new StringBuilder();
        for (char c : st) sb.append(c);
        return sb.toString();
    }
}
