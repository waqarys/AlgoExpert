# 0070. Climbing Stairs

**Difficulty:** Easy | **Category:** 1-D Dynamic Programming | **LeetCode:** https://leetcode.com/problems/climbing-stairs/

## Problem
- You climb 1 or 2 steps at a time. How many distinct ways reach step n?

## Intuition
- The last move onto step n came from n-1 or n-2, so ways(n) = ways(n-1) + ways(n-2): Fibonacci.
- Only the previous two values are needed.

## Brute Force
- Plain recursion without memo: O(2^n).

## Optimal Approach
1. a = 1 (ways to reach step 0), b = 1 (step 1).
2. Repeat n-1 times: (a, b) = (b, a + b).
3. Return b.

## Worked Example
- n = 5.
```text
step: 0 1 2 3 4 5
ways: 1 1 2 3 5 8
```

## Complexity
- Time: O(n). Space: O(1).

## Pitfalls
- Base cases: n = 1 -> 1, n = 2 -> 2.

## Video Script
- DP intro: recursion tree -> memo -> bottom-up -> two variables.

## Solution
```java file=dp1/ClimbingStairs.java
package dp1;

/**
 * LC 70 Climbing Stairs.
 * Approach: Fibonacci recurrence ways(n) = ways(n-1) + ways(n-2) with two variables.
 * Time O(n), Space O(1).
 */
public class ClimbingStairs {
    public int climbStairs(int n) {
        int a = 1, b = 1;
        for (int i = 2; i <= n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
}
```

## Tests
```java test=dp1/ClimbingStairsTest.java
package dp1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ClimbingStairsTest {
    ClimbingStairs s = new ClimbingStairs();
    @Test void examples() {
        assertEquals(1, s.climbStairs(1));
        assertEquals(2, s.climbStairs(2));
        assertEquals(3, s.climbStairs(3));
        assertEquals(8, s.climbStairs(5));
        assertEquals(1836311903, s.climbStairs(45));
    }
}
```
