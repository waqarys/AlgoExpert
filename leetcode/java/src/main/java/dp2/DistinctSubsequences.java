package dp2;

/**
 * LC 115 Distinct Subsequences.
 * Approach: dp[j] = ways to form t[0..j) from the processed prefix of s; iterate j downward.
 * Time O(mn), Space O(n).
 */
public class DistinctSubsequences {
    public int numDistinct(String s, String t) {
        int n = t.length();
        long[] dp = new long[n + 1];
        dp[0] = 1;
        for (int i = 0; i < s.length(); i++)
            for (int j = n; j >= 1; j--)
                if (s.charAt(i) == t.charAt(j - 1)) dp[j] += dp[j - 1];
        return (int) dp[n];
    }
}
