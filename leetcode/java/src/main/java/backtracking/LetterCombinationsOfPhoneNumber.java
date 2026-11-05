package backtracking;

import java.util.*;

/**
 * LC 17 Letter Combinations of a Phone Number.
 * Approach: backtracking with one level per digit.
 * Time O(4^n * n), Space O(n).
 */
public class LetterCombinationsOfPhoneNumber {
    private static final String[] MAP = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        List<String> res = new ArrayList<>();
        if (digits.isEmpty()) return res;
        dfs(digits, 0, new StringBuilder(), res);
        return res;
    }

    private void dfs(String d, int i, StringBuilder sb, List<String> res) {
        if (i == d.length()) { res.add(sb.toString()); return; }
        for (char ch : MAP[d.charAt(i) - '0'].toCharArray()) {
            sb.append(ch);
            dfs(d, i + 1, sb, res);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}
