package dp1;

/**
 * LC 746 Min Cost Climbing Stairs.
 * Approach: dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]) rolled into two variables.
 * Time O(n), Space O(1).
 */
public class MinCostClimbingStairs {
    public int minCostClimbingStairs(int[] cost) {
        int a = 0, b = 0;
        for (int i = 2; i <= cost.length; i++) {
            int c = Math.min(b + cost[i - 1], a + cost[i - 2]);
            a = b;
            b = c;
        }
        return b;
    }
}
