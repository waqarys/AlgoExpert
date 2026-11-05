package dp1;

import java.util.*;

/**
 * LC 322 Coin Change.
 * Approach: unbounded-knapsack DP, dp[a] = 1 + min dp[a - coin].
 * Time O(amount * coins), Space O(amount).
 */
public class CoinChange {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        for (int a = 1; a <= amount; a++)
            for (int c : coins)
                if (c <= a) dp[a] = Math.min(dp[a], dp[a - c] + 1);
        return dp[amount] > amount ? -1 : dp[amount];
    }
}
