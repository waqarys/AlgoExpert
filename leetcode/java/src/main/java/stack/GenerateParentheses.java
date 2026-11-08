package stack;

import java.util.*;

/**
 * LC 22 Generate Parentheses.
 * Approach: backtracking; add '(' while open < n, ')' while close < open.
 * Time O(Catalan(n) * n), Space O(n).
 */
public class GenerateParentheses {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        go(new StringBuilder(), 0, 0, n, res);
        return res;
    }

    private void go(StringBuilder sb, int open, int close, int n, List<String> res) {
        if (sb.length() == 2 * n) { res.add(sb.toString()); return; }
        if (open < n) { sb.append('('); go(sb, open + 1, close, n, res); sb.deleteCharAt(sb.length() - 1); }
        if (close < open) { sb.append(')'); go(sb, open, close + 1, n, res); sb.deleteCharAt(sb.length() - 1); }
    }
}
