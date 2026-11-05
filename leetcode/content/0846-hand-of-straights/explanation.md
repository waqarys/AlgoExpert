# 0846. Hand of Straights

**Difficulty:** Medium | **Category:** Greedy | **LeetCode:** https://leetcode.com/problems/hand-of-straights/

## Problem
- Can the cards be rearranged into groups of groupSize consecutive values?

## Intuition
- The smallest remaining card must start a group (nothing smaller can include it).
- So repeatedly take the smallest card x and consume x, x+1, ..., x+size-1.

## Brute Force
- Backtracking over groupings: exponential.

## Optimal Approach
1. If n % size != 0 return false.
2. TreeMap value -> count.
3. While the map is non-empty: x = firstKey; for v = x..x+size-1: if v is missing return false; decrement (remove at 0).

## Worked Example
- [1,2,3,6,2,3,4,7,8], size 3.
```text
smallest 1 -> take 1,2,3   left {2,3,4,6,7,8}
smallest 2 -> take 2,3,4   left {6,7,8}
smallest 6 -> take 6,7,8   done -> true
```

## Complexity
- Time: O(n log n). Space: O(n).

## Pitfalls
- Same problem as LC 1296 (Divide Array in Sets of K Consecutive Numbers).

## Video Script
- Greedy justification: "the smallest card has no choice".

## Solution
```java file=greedy/HandOfStraights.java
package greedy;

import java.util.*;

/**
 * LC 846 Hand of Straights.
 * Approach: TreeMap counts; the smallest remaining card always starts a group.
 * Time O(n log n), Space O(n).
 */
public class HandOfStraights {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        if (hand.length % groupSize != 0) return false;
        TreeMap<Integer, Integer> count = new TreeMap<>();
        for (int c : hand) count.merge(c, 1, Integer::sum);
        while (!count.isEmpty()) {
            int x = count.firstKey();
            for (int v = x; v < x + groupSize; v++) {
                Integer c = count.get(v);
                if (c == null) return false;
                if (c == 1) count.remove(v);
                else count.put(v, c - 1);
            }
        }
        return true;
    }
}
```

## Tests
```java test=greedy/HandOfStraightsTest.java
package greedy;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class HandOfStraightsTest {
    HandOfStraights s = new HandOfStraights();
    @Test void examples() {
        assertTrue(s.isNStraightHand(new int[]{1, 2, 3, 6, 2, 3, 4, 7, 8}, 3));
        assertFalse(s.isNStraightHand(new int[]{1, 2, 3, 4, 5}, 4));
        assertTrue(s.isNStraightHand(new int[]{8, 10, 12}, 1));
        assertFalse(s.isNStraightHand(new int[]{1, 1, 2, 3}, 2));
    }
}
```
