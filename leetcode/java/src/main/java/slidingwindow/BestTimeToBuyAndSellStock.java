package slidingwindow;

/**
 * LC 121 Best Time to Buy and Sell Stock.
 * Approach: track the running minimum price; profit = price - min.
 * Time O(n), Space O(1).
 */
public class BestTimeToBuyAndSellStock {
    public int maxProfit(int[] prices) {
        int min = Integer.MAX_VALUE, best = 0;
        for (int p : prices) {
            min = Math.min(min, p);
            best = Math.max(best, p - min);
        }
        return best;
    }
}
