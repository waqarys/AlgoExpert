package dp2;

/**
 * LC 97 Interleaving String.
 * Approach: dp[i][j] over prefixes of s1 and s2, compressed to one row.
 * Time O(mn), Space O(n).
 */
public class InterleavingString {
    public boolean isInterleave(String s1, String s2, String s3) {
        int m = s1.length(), n = s2.length();
        if (m + n != s3.length()) return false;
        boolean[] dp = new boolean[n + 1];
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0 && j == 0) { dp[0] = true; continue; }
                char c = s3.charAt(i + j - 1);
                boolean fromS1 = i > 0 && dp[j] && s1.charAt(i - 1) == c;
                boolean fromS2 = j > 0 && dp[j - 1] && s2.charAt(j - 1) == c;
                dp[j] = fromS1 || fromS2;
            }
        }
        return dp[n];
    }
}
