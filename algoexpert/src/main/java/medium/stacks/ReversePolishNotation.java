package medium.stacks;

import java.util.ArrayDeque;

/**
 * Reverse Polish Notation: evaluate postfix tokens with + - * / (integer division truncating toward zero).
 * Time: O(n) | Space: O(n).
 */
public class ReversePolishNotation {
    public static int reversePolishNotation(String[] tokens) {
        ArrayDeque<Integer> st = new ArrayDeque<>();
        for (String t : tokens) {
            switch (t) {
                case "+" -> st.push(st.pop() + st.pop());
                case "*" -> st.push(st.pop() * st.pop());
                case "-" -> { int b = st.pop(); st.push(st.pop() - b); }
                case "/" -> { int b = st.pop(); st.push(st.pop() / b); }
                default -> st.push(Integer.parseInt(t));
            }
        }
        return st.pop();
    }
}
