# 0050. Pow(x, n)

**Difficulty:** Medium | **Category:** Math & Geometry | **LeetCode:** https://leetcode.com/problems/powx-n/

## Problem
- Compute x raised to the integer power n (n may be negative).

## Intuition
- Fast exponentiation: x^n = (x^2)^(n/2), times x if n is odd. Halving n each step gives O(log n).
- Negative n: compute (1/x)^(-n).

## Brute Force
- Multiply n times: O(n), too slow for n near 2^31.

## Optimal Approach
1. e = (long) n; if e < 0: x = 1/x, e = -e.
2. res = 1. While e > 0: if e is odd, res *= x; x *= x; e >>= 1.

## Worked Example
- x = 2, n = 10 (binary 1010).
```text
e=10 even          x=4
e=5  odd  res=4    x=16
e=2  even          x=256
e=1  odd  res=1024
```

## Complexity
- Time: O(log n). Space: O(1).

## Pitfalls
- -Integer.MIN_VALUE overflows int; convert to long first.

## Video Script
- Binary exponentiation shows up everywhere, from cryptography to matrix Fibonacci.

## Solution
```java file=math/PowXN.java
package math;

/**
 * LC 50 Pow(x, n).
 * Approach: iterative binary exponentiation; a long exponent avoids MIN_VALUE overflow.
 * Time O(log n), Space O(1).
 */
public class PowXN {
    public double myPow(double x, int n) {
        long e = n;
        if (e < 0) { x = 1 / x; e = -e; }
        double res = 1;
        while (e > 0) {
            if ((e & 1) == 1) res *= x;
            x *= x;
            e >>= 1;
        }
        return res;
    }
}
```

## Tests
```java test=math/PowXNTest.java
package math;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class PowXNTest {
    PowXN s = new PowXN();
    @Test void examples() {
        assertEquals(1024.0, s.myPow(2.0, 10), 1e-9);
        assertEquals(9.261, s.myPow(2.1, 3), 1e-9);
        assertEquals(0.25, s.myPow(2.0, -2), 1e-9);
        assertEquals(1.0, s.myPow(1.0, Integer.MIN_VALUE), 1e-9);
        assertEquals(1.0, s.myPow(5.0, 0), 1e-9);
    }
}
```
