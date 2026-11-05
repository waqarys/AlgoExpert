package dp2;

/**
 * LC 10 Regular Expression Matching.
 * Approach: 2-D DP over prefixes; '*' = zero copies (j-2) or one more copy (i-1).
 * Time O(mn), Space O(mn).
 */
public class RegularExpressionMatching {
    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[0][0] = true;
        for (int j = 2; j <= n; j++) dp[0][j] = p.charAt(j - 1) == '*' && dp[0][j - 2];
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++) {
                char pc = p.charAt(j - 1);
                if (pc == '*') {
                    dp[i][j] = dp[i][j - 2] || (matches(s.charAt(i - 1), p.charAt(j - 2)) && dp[i - 1][j]);
                } else {
                    dp[i][j] = matches(s.charAt(i - 1), pc) && dp[i - 1][j - 1];
                }
            }
        return dp[m][n];
    }

    private boolean matches(char sc, char pc) { return pc == '.' || pc == sc; }
}
