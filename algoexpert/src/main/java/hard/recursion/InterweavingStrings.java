package hard.recursion;

/**
 * Interweaving Strings: can `three` be formed by interleaving `one` and `two` keeping each one's order?
 * Time: O(n*m) | Space: O(m).
 */
public class InterweavingStrings {
    public static boolean interweavingStrings(String one, String two, String three) {
        int n = one.length(), m = two.length();
        if (n + m != three.length()) return false;
        boolean[] dp = new boolean[m + 1];
        for (int i = 0; i <= n; i++)
            for (int j = 0; j <= m; j++) {
                if (i == 0 && j == 0) { dp[0] = true; continue; }
                boolean fromOne = i > 0 && dp[j] && one.charAt(i - 1) == three.charAt(i + j - 1);
                boolean fromTwo = j > 0 && dp[j - 1] && two.charAt(j - 1) == three.charAt(i + j - 1);
                dp[j] = fromOne || fromTwo;
            }
        return dp[m];
    }
}
