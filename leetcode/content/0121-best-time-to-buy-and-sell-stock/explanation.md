# 0121. Best Time to Buy and Sell Stock

**Difficulty:** Easy | **Category:** Sliding Window | **LeetCode:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Problem
- prices[i] is the price on day i. Buy once and sell once later; return the max profit (0 if none).
- Example: [7,1,5,3,6,4] -> 5 (buy at 1, sell at 6).

## Intuition
- For each selling day, the best buy is the minimum price seen so far.
- Track that running minimum (the window's left edge) and the best difference.

## Brute Force
- All pairs i < j: O(n^2).

## Optimal Approach
1. minPrice = +infinity, best = 0.
2. For each p: minPrice = min(minPrice, p); best = max(best, p - minPrice).

## Worked Example
- prices = [7,1,5,3,6,4].
```text
p=7 min=7 best=0
p=1 min=1 best=0
p=5 min=1 best=4
p=3 min=1 best=4
p=6 min=1 best=5
p=4 min=1 best=5
```

## Complexity
- Time: O(n). Space: O(1).

## Pitfalls
- You cannot sell before buying, so a later minimum must not pair with an earlier price.

## Video Script
- Frame it as a sliding window whose left edge jumps to any new low.

## Solution
```java file=slidingwindow/BestTimeToBuyAndSellStock.java
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
```

## Tests
```java test=slidingwindow/BestTimeToBuyAndSellStockTest.java
package slidingwindow;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class BestTimeToBuyAndSellStockTest {
    BestTimeToBuyAndSellStock s = new BestTimeToBuyAndSellStock();
    @Test void examples() {
        assertEquals(5, s.maxProfit(new int[]{7, 1, 5, 3, 6, 4}));
        assertEquals(0, s.maxProfit(new int[]{7, 6, 4, 3, 1}));
        assertEquals(0, s.maxProfit(new int[]{5}));
        assertEquals(4, s.maxProfit(new int[]{2, 4, 1, 5}));
    }
}
```
