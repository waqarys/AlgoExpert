package hard.dynamicprogramming;

import java.util.ArrayList;
import java.util.List;

/**
 * Juice Bottling: prices[i] is the price of a bottle of size i (prices[0] = 0). Split the total
 * (prices.length - 1 units) into bottle sizes maximising revenue; return sizes (rod cutting).
 * Time: O(n^2) | Space: O(n).
 */
public class JuiceBottling {
    public static List<Integer> juiceBottling(int[] prices) {
        int n = prices.length;
        int[] best = new int[n], cut = new int[n];
        for (int s = 1; s < n; s++)
            for (int k = 1; k <= s; k++)
                if (prices[k] + best[s - k] > best[s]) { best[s] = prices[k] + best[s - k]; cut[s] = k; }
        List<Integer> out = new ArrayList<>();
        for (int s = n - 1; s > 0; s -= cut[s]) out.add(cut[s]);
        return out;
    }
}
