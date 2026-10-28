package hard.dynamicprogramming;

import java.util.ArrayList;
import java.util.List;

/**
 * Longest Common Subsequence: one LCS of two strings as a list of chars.
 * Time: O(n*m) | Space: O(n*m).
 */
public class LongestCommonSubsequence {
    public static List<Character> longestCommonSubsequence(String a, String b) {
        int n = a.length(), m = b.length();
        int[][] dp = new int[n + 1][m + 1];
        for (int i = 1; i <= n; i++) for (int j = 1; j <= m; j++)
            dp[i][j] = a.charAt(i - 1) == b.charAt(j - 1) ? dp[i - 1][j - 1] + 1 : Math.max(dp[i - 1][j], dp[i][j - 1]);
        List<Character> out = new ArrayList<>();
        int i = n, j = m;
        while (i > 0 && j > 0) {
            if (a.charAt(i - 1) == b.charAt(j - 1)) { out.add(0, a.charAt(i - 1)); i--; j--; }
            else if (dp[i - 1][j] >= dp[i][j - 1]) i--; else j--;
        }
        return out;
    }
}
