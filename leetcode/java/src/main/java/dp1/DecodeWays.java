package dp1;

/**
 * LC 91 Decode Ways.
 * Approach: dp over prefixes with one-digit and two-digit transitions.
 * Time O(n), Space O(1).
 */
public class DecodeWays {
    public int numDecodings(String s) {
        int prev2 = 1, prev1 = s.charAt(0) == '0' ? 0 : 1; // dp[0], dp[1]
        for (int i = 2; i <= s.length(); i++) {
            int cur = 0;
            if (s.charAt(i - 1) != '0') cur += prev1;
            int two = (s.charAt(i - 2) - '0') * 10 + (s.charAt(i - 1) - '0');
            if (two >= 10 && two <= 26) cur += prev2;
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }
}
