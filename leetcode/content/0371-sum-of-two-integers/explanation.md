# 0371. Sum of Two Integers

**Difficulty:** Medium | **Category:** Bit Manipulation | **LeetCode:** https://leetcode.com/problems/sum-of-two-integers/

## Problem
- Add two integers without using + or -.

## Intuition
- a ^ b adds the bits without carries, and (a & b) << 1 is exactly the carry.
- Repeat with (sum, carry) until the carry is 0. Two's complement makes negatives work for free with Java's 32-bit ints.

## Brute Force
- Increment in a loop: O(|b|), and it still uses ++.

## Optimal Approach
1. While b != 0: carry = (a & b) << 1; a = a ^ b; b = carry.
2. Return a.

## Worked Example
- a = 2 (10), b = 3 (11).
```text
xor=01  carry=100   a=1 b=4
xor=101 carry=0     a=5 b=0
answer 5
```

## Complexity
- Time: O(32). Space: O(1).

## Pitfalls
- In Python you must mask to 32 bits; Java ints wrap naturally.

## Video Script
- Build a half adder from XOR and AND, then loop it.

## Solution
```java file=bits/SumOfTwoIntegers.java
package bits;

/**
 * LC 371 Sum of Two Integers.
 * Approach: XOR for the sum without carry, AND<<1 for the carry; loop until no carry.
 * Time O(32), Space O(1).
 */
public class SumOfTwoIntegers {
    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            a ^= b;
            b = carry;
        }
        return a;
    }
}
```

## Tests
```java test=bits/SumOfTwoIntegersTest.java
package bits;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SumOfTwoIntegersTest {
    SumOfTwoIntegers s = new SumOfTwoIntegers();
    @Test void examples() {
        assertEquals(3, s.getSum(1, 2));
        assertEquals(5, s.getSum(2, 3));
        assertEquals(-1, s.getSum(-3, 2));
        assertEquals(-1000, s.getSum(-1000, 0));
        assertEquals(0, s.getSum(-7, 7));
    }
}
```
