# 0518. Coin Change II

**Difficulty:** Medium | **Category:** 2-D Dynamic Programming | **LeetCode:** https://leetcode.com/problems/coin-change-ii/

## Problem
- Count the combinations (order does not matter) of coins that sum to amount. Unlimited supply.

## Intuition
- Process coins one at a time in the outer loop: ways[a] += ways[a - coin]. Since each coin is introduced once, combinations are counted in a fixed coin order, so permutations are not double counted.

## Brute Force
- Backtracking with a non-decreasing coin index: exponential.

## Optimal Approach
1. ways[0] = 1.
2. For coin c: for a = c..amount: ways[a] += ways[a - c].

## Worked Example
- amount 5, coins [1,2,5].
```text
after 1: ways = 1 1 1 1 1 1
after 2: ways = 1 1 2 2 3 3
after 5: ways = 1 1 2 2 3 4   -> 4
```

## Complexity
- Time: O(amount * coins). Space: O(amount).

## Pitfalls
- Swapping the loops (amount outer, coins inner) counts permutations instead (that is Combination Sum IV).

## Video Script
- Show both loop orders and their different answers for amount 3 with [1,2].

## Solution
```java file=dp2/CoinChangeII.java
package dp2;

/**
 * LC 518 Coin Change II.
 * Approach: unbounded knapsack counting; coins in the outer loop to count combinations.
 * Time O(amount * coins), Space O(amount).
 */
public class CoinChangeII {
    public int change(int amount, int[] coins) {
        int[] ways = new int[amount + 1];
        ways[0] = 1;
        for (int c : coins)
            for (int a = c; a <= amount; a++) ways[a] += ways[a - c];
        return ways[amount];
    }
}
```

## Tests
```java test=dp2/CoinChangeIITest.java
package dp2;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CoinChangeIITest {
    CoinChangeII s = new CoinChangeII();
    @Test void examples() {
        assertEquals(4, s.change(5, new int[]{1, 2, 5}));
        assertEquals(0, s.change(3, new int[]{2}));
        assertEquals(1, s.change(10, new int[]{10}));
        assertEquals(1, s.change(0, new int[]{7}));
    }
}
```
