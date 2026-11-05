# 0191. Number of 1 Bits

**Difficulty:** Easy | **Category:** Bit Manipulation | **LeetCode:** https://leetcode.com/problems/number-of-1-bits/

## Problem
- Return the number of set bits (Hamming weight) of an integer treated as unsigned 32-bit.

## Intuition
- n & (n - 1) clears the lowest set bit. Count how many times we can do that before n is 0.

## Brute Force
- Check all 32 bits with (n >>> i) & 1.

## Optimal Approach
1. count = 0; while n != 0: n &= n - 1; count++.

## Worked Example
- n = 11 (1011).
```text
1011 & 1010 = 1010  count 1
1010 & 1001 = 1000  count 2
1000 & 0111 = 0000  count 3
```

## Complexity
- Time: O(number of set bits). Space: O(1).

## Pitfalls
- Use n != 0, not n > 0: negative ints have the sign bit set.

## Video Script
- The n & (n-1) trick, shown bit by bit.

## Solution
```java file=bits/NumberOf1Bits.java
package bits;

/**
 * LC 191 Number of 1 Bits.
 * Approach: Brian Kernighan's trick, n &= n - 1 clears the lowest set bit.
 * Time O(set bits), Space O(1).
 */
public class NumberOf1Bits {
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) { n &= n - 1; count++; }
        return count;
    }
}
```

## Tests
```java test=bits/NumberOf1BitsTest.java
package bits;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class NumberOf1BitsTest {
    NumberOf1Bits s = new NumberOf1Bits();
    @Test void examples() {
        assertEquals(3, s.hammingWeight(11));
        assertEquals(1, s.hammingWeight(128));
        assertEquals(31, s.hammingWeight(0xFFFFFFFD));
        assertEquals(0, s.hammingWeight(0));
    }
}
```
