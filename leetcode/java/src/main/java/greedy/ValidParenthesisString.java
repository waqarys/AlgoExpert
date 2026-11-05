package greedy;

/**
 * LC 678 Valid Parenthesis String.
 * Approach: maintain the range [lo, hi] of possible open counts.
 * Time O(n), Space O(1).
 */
public class ValidParenthesisString {
    public boolean checkValidString(String s) {
        int lo = 0, hi = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') { lo++; hi++; }
            else if (c == ')') { lo--; hi--; }
            else { lo--; hi++; }
            if (hi < 0) return false;
            lo = Math.max(lo, 0);
        }
        return lo == 0;
    }
}
