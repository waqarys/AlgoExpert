package string;

import java.util.Stack;

/**
 * Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
 * Note that after backspacing an empty text, the text will continue empty.
 *
 * Example 1:
 *
 * Input: s = "ab#c", t = "ad#c"
 * Output: true
 * Explanation: Both s and t become "ac".
 *
 * Example 2:
 *
 * Input: s = "ab##", t = "c#d#"
 * Output: true
 * Explanation: Both s and t become "".
 *
 * Example 3:
 *
 * Input: s = "a#c", t = "b"
 * Output: false
 * Explanation: s becomes "c" while t becomes "b".
 *
 * Constraints:
 *
 *     1 <= s.length, t.length <= 200
 *     s and t only contain lowercase letters and '#' characters.
 */
public class BackspaceCompare {

    public boolean backspaceCompare(String s, String t) {
        Stack<Character> first = new Stack<>();
        Stack<Character> second = new Stack<>();
        first = populateStack(s);
        second = populateStack(t);

        while (!first.isEmpty()) {
            char cur= first.pop();
            if(second.isEmpty() || cur != second.pop()) {
                return false;
            }
        }

        return second.isEmpty();
    }

    private Stack<Character> populateStack(String s) {
        Stack<Character> stack = new Stack();
        for(char c : s.toCharArray()) {
            if(c == '#') {
                if(!stack.isEmpty()) {
                    stack.pop();
                }
            } else {
                stack.push(c);
            }
        }
        return stack;
    }
}
