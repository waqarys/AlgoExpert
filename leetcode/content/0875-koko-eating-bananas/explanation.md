# 0875. Koko Eating Bananas

**Difficulty:** Medium | **Category:** Binary Search | **LeetCode:** https://leetcode.com/problems/koko-eating-bananas/

## Problem
- piles[i] bananas; each hour Koko eats up to k bananas from one pile. Find the minimum k to finish within h hours.
- Example: piles [3,6,7,11], h = 8 -> 4.

## Intuition
- If speed k works, any faster speed also works: feasibility is monotonic in k.
- So binary search on the answer space [1, max(pile)] for the first feasible k.

## Brute Force
- Try k = 1, 2, ... until feasible: O(max * n).

## Optimal Approach
1. lo = 1, hi = max(piles).
2. hours(k) = sum of ceil(p / k) = sum (p + k - 1) / k.
3. If hours(mid) <= h, hi = mid (mid might be the answer); else lo = mid + 1. Return lo.

## Worked Example
- piles [3,6,7,11], h = 8.
```text
lo=1 hi=11 mid=6  hours=1+1+2+2=6  <=8 -> hi=6
lo=1 hi=6  mid=3  hours=1+2+3+4=10 >8  -> lo=4
lo=4 hi=6  mid=5  hours=1+2+2+3=8  <=8 -> hi=5
lo=4 hi=5  mid=4  hours=1+2+2+3=8  <=8 -> hi=4
answer 4
```

## Complexity
- Time: O(n log max). Space: O(1).

## Pitfalls
- Hours can exceed int range for large piles with small k; sum into a long.

## Video Script
- Introduce "binary search on the answer": monotonic predicate + lower-bound template.

## Solution
```java file=binarysearch/KokoEatingBananas.java
package binarysearch;

/**
 * LC 875 Koko Eating Bananas.
 * Approach: binary search the smallest speed k whose total hours <= h (monotonic predicate).
 * Time O(n log max), Space O(1).
 */
public class KokoEatingBananas {
    public int minEatingSpeed(int[] piles, int h) {
        int lo = 1, hi = 0;
        for (int p : piles) hi = Math.max(hi, p);
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (hours(piles, mid) <= h) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private long hours(int[] piles, int k) {
        long total = 0;
        for (int p : piles) total += (p + (long) k - 1) / k;
        return total;
    }
}
```

## Tests
```java test=binarysearch/KokoEatingBananasTest.java
package binarysearch;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class KokoEatingBananasTest {
    KokoEatingBananas s = new KokoEatingBananas();
    @Test void examples() {
        assertEquals(4, s.minEatingSpeed(new int[]{3, 6, 7, 11}, 8));
        assertEquals(30, s.minEatingSpeed(new int[]{30, 11, 23, 4, 20}, 5));
        assertEquals(23, s.minEatingSpeed(new int[]{30, 11, 23, 4, 20}, 6));
        assertEquals(3, s.minEatingSpeed(new int[]{805306368, 805306368, 805306368}, 1000000000));
    }
}
```
