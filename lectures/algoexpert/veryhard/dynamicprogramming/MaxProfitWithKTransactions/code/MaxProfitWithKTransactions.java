public class MaxProfitWithKTransactions {
    public static int maxProfitWithKTransactions(int[] prices, int k) {
        if (prices.length == 0) return 0;
        int[] prev = new int[prices.length], cur = new int[prices.length];
        for (int t = 1; t <= k; t++) {
            int bestBuy = Integer.MIN_VALUE;
            for (int d = 0; d < prices.length; d++) {
                bestBuy = Math.max(bestBuy, prev[d] - prices[d]);
                cur[d] = Math.max(d > 0 ? cur[d - 1] : 0, bestBuy + prices[d]);
            }
            int[] tmp = prev; prev = cur; cur = tmp;
        }
        return prev[prices.length - 1];
    }
}
