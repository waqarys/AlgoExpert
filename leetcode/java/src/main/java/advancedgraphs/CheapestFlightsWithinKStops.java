package advancedgraphs;

import java.util.*;

/**
 * LC 787 Cheapest Flights Within K Stops.
 * Approach: Bellman-Ford for k+1 rounds, relaxing from a snapshot each round.
 * Time O(k * E), Space O(n).
 */
public class CheapestFlightsWithinKStops {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int[] prices = new int[n];
        Arrays.fill(prices, Integer.MAX_VALUE);
        prices[src] = 0;
        for (int round = 0; round <= k; round++) {
            int[] tmp = prices.clone();
            for (int[] f : flights) {
                if (prices[f[0]] == Integer.MAX_VALUE) continue;
                tmp[f[1]] = Math.min(tmp[f[1]], prices[f[0]] + f[2]);
            }
            prices = tmp;
        }
        return prices[dst] == Integer.MAX_VALUE ? -1 : prices[dst];
    }
}
