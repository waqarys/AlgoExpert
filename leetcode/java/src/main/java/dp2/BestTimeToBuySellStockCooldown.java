package dp2;

/**
 * LC 309 Best Time to Buy and Sell Stock with Cooldown.
 * Approach: 3-state machine (hold, sold, rest) updated per day.
 * Time O(n), Space O(1).
 */
public class BestTimeToBuySellStockCooldown {
    public int maxProfit(int[] prices) {
        if (prices.length == 0) return 0;
        int hold = -prices[0], sold = 0, rest = 0;
        for (int i = 1; i < prices.length; i++) {
            int p = prices[i];
            int newHold = Math.max(hold, rest - p);
            int newSold = hold + p;
            int newRest = Math.max(rest, sold);
            hold = newHold;
            sold = newSold;
            rest = newRest;
        }
        return Math.max(sold, rest);
    }
}
