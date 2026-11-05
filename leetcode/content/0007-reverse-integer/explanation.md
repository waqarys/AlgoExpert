# 0007. Reverse Integer

**Difficulty:** Medium | **Category:** Bit Manipulation | **LeetCode:** https://leetcode.com/problems/reverse-integer/

## Problem
- Reverse the digits of a 32-bit signed integer. Return 0 if the result overflows. You may not use 64-bit integers.

## Intuition
- Pop digits with % 10 and push them with res * 10 + d.
- Before pushing, check whether res * 10 + d would leave the int range.

## Brute Force
- Use a long or a string reversal: forbidden by the 32-bit constraint.

## Optimal Approach
1. While x != 0: d = x % 10; x /= 10.
2. If res > MAX/10, or res == MAX/10 and d > 7, return 0; mirror the check for MIN with -8.
3. res = res * 10 + d.

## Worked Example
- x = -123.
```text
d=-3 res=-3
d=-2 res=-32
d=-1 res=-321
```
- x = 1534236469 would reverse to 9646324351 > MAX, so the answer is 0.

## Complexity
- Time: O(log |x|). Space: O(1).

## Pitfalls
- Java % keeps the sign of x, so negatives need no special handling.

## Video Script
- Teach checking for overflow before the operation, a common interview follow-up.

## Solution
```java file=bits/ReverseInteger.java
package bits;

/**
 * LC 7 Reverse Integer.
 * Approach: pop/push digits with a pre-multiplication overflow check (no 64-bit math).
 * Time O(log x), Space O(1).
 */
public class ReverseInteger {
    public int reverse(int x) {
        int res = 0;
        while (x != 0) {
            int d = x % 10;
            x /= 10;
            if (res > Integer.MAX_VALUE / 10 || (res == Integer.MAX_VALUE / 10 && d > 7)) return 0;
            if (res < Integer.MIN_VALUE / 10 || (res == Integer.MIN_VALUE / 10 && d < -8)) return 0;
            res = res * 10 + d;
        }
        return res;
    }
}
```

## Tests
```java test=bits/ReverseIntegerTest.java
package bits;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ReverseIntegerTest {
    ReverseInteger s = new ReverseInteger();
    @Test void examples() {
        assertEquals(321, s.reverse(123));
        assertEquals(-321, s.reverse(-123));
        assertEquals(21, s.reverse(120));
        assertEquals(0, s.reverse(1534236469));
        assertEquals(0, s.reverse(Integer.MIN_VALUE));
        assertEquals(0, s.reverse(0));
    }
}
```
