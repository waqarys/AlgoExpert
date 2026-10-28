package medium.dynamicprogramming;

import java.util.Arrays;

/**
 * Min Number Of Coins For Change: fewest coins summing to n, or -1 if impossible.
 * Time: O(n*d) | Space: O(n).
 */
public class MinNumberOfCoinsForChange {
    public static int minNumberOfCoinsForChange(int n, int[] denoms) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        for (int d : denoms)
            for (int a = d; a <= n; a++)
                if (dp[a - d] != Integer.MAX_VALUE) dp[a] = Math.min(dp[a], dp[a - d] + 1);
        return dp[n] == Integer.MAX_VALUE ? -1 : dp[n];
    }
}
