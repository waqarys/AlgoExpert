# 0338. Counting Bits

**Difficulty:** Easy | **Category:** Bit Manipulation | **LeetCode:** https://leetcode.com/problems/counting-bits/

## Problem
- For every i in 0..n, return the number of 1 bits in i, in O(n).

## Intuition
- i >> 1 has the same bits as i except the last one, so bits[i] = bits[i >> 1] + (i & 1).

## Brute Force
- Popcount each i separately: O(n log n).

## Optimal Approach
1. bits[0] = 0.
2. For i = 1..n: bits[i] = bits[i >> 1] + (i & 1).

## Worked Example
- n = 5.
```text
i:    0 1 2 3 4 5
bits: 0 1 1 2 1 2
bits[5] = bits[2] + 1 = 2
```

## Complexity
- Time: O(n). Space: O(n) for the output.

## Pitfalls
- An alternative recurrence is bits[i] = bits[i & (i-1)] + 1.

## Video Script
- DP meets bit manipulation.

## Solution
```java file=bits/CountingBits.java
package bits;

/**
 * LC 338 Counting Bits.
 * Approach: DP bits[i] = bits[i >> 1] + (i & 1).
 * Time O(n), Space O(n).
 */
public class CountingBits {
    public int[] countBits(int n) {
        int[] bits = new int[n + 1];
        for (int i = 1; i <= n; i++) bits[i] = bits[i >> 1] + (i & 1);
        return bits;
    }
}
```

## Tests
```java test=bits/CountingBitsTest.java
package bits;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CountingBitsTest {
    CountingBits s = new CountingBits();
    @Test void examples() {
        assertArrayEquals(new int[]{0, 1, 1}, s.countBits(2));
        assertArrayEquals(new int[]{0, 1, 1, 2, 1, 2}, s.countBits(5));
        assertArrayEquals(new int[]{0}, s.countBits(0));
    }
}
```
