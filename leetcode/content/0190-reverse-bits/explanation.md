# 0190. Reverse Bits

**Difficulty:** Easy | **Category:** Bit Manipulation | **LeetCode:** https://leetcode.com/problems/reverse-bits/

## Problem
- Reverse the 32 bits of an unsigned integer.

## Intuition
- Read bits from the right end of n and push them onto the right end of the result, 32 times; the first bit read ends up leftmost.

## Brute Force
- Convert to a binary string, pad, reverse and parse: works, but slow and clunky.

## Optimal Approach
1. res = 0.
2. Repeat 32 times: res = (res << 1) | (n & 1); n >>>= 1.

## Worked Example
- 8-bit illustration: 00001101.
```text
take 1 -> 1
take 0 -> 10
take 1 -> 101
take 1 -> 1011
take 0 x4 -> 10110000
```

## Complexity
- Time: O(32). Space: O(1).

## Pitfalls
- Use the unsigned shift >>> so the sign bit does not smear.

## Video Script
- Show the shifts like moving beads from one abacus to another.

## Solution
```java file=bits/ReverseBits.java
package bits;

/**
 * LC 190 Reverse Bits.
 * Approach: pop the low bit of n, push it onto res, 32 times.
 * Time O(32), Space O(1).
 */
public class ReverseBits {
    public int reverseBits(int n) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            res = (res << 1) | (n & 1);
            n >>>= 1;
        }
        return res;
    }
}
```

## Tests
```java test=bits/ReverseBitsTest.java
package bits;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ReverseBitsTest {
    ReverseBits s = new ReverseBits();
    @Test void examples() {
        assertEquals(964176192, s.reverseBits(0b00000010100101000001111010011100));
        assertEquals(-1073741825, s.reverseBits(0b11111111111111111111111111111101));
        assertEquals(Integer.MIN_VALUE, s.reverseBits(1));
    }
}
```
