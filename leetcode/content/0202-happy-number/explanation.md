# 0202. Happy Number

**Difficulty:** Easy | **Category:** Math & Geometry | **LeetCode:** https://leetcode.com/problems/happy-number/

## Problem
- Repeatedly replace n with the sum of the squares of its digits. n is happy if this reaches 1; otherwise it loops forever.

## Intuition
- The sequence either reaches 1 or enters a cycle. Detect the cycle with Floyd's slow/fast pointers (or a HashSet).

## Brute Force
- A HashSet of seen values uses extra space.

## Optimal Approach
1. slow = n, fast = next(n).
2. While fast != 1 and slow != fast: slow = next(slow); fast = next(next(fast)).
3. Return fast == 1.

## Worked Example
- n = 19.
```text
19  -> 1 + 81  = 82
82  -> 64 + 4  = 68
68  -> 36 + 64 = 100
100 -> 1   -> happy
```

## Complexity
- Time: O(log n) per step, with few steps. Space: O(1).

## Pitfalls
- n = 1 is happy immediately.

## Video Script
- Reuse Linked List Cycle on a number sequence.

## Solution
```java file=math/HappyNumber.java
package math;

/**
 * LC 202 Happy Number.
 * Approach: Floyd's cycle detection on the digit-square-sum sequence.
 * Time O(log n), Space O(1).
 */
public class HappyNumber {
    public boolean isHappy(int n) {
        int slow = n, fast = next(n);
        while (fast != 1 && slow != fast) {
            slow = next(slow);
            fast = next(next(fast));
        }
        return fast == 1;
    }

    private int next(int n) {
        int s = 0;
        while (n > 0) { int d = n % 10; s += d * d; n /= 10; }
        return s;
    }
}
```

## Tests
```java test=math/HappyNumberTest.java
package math;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class HappyNumberTest {
    HappyNumber s = new HappyNumber();
    @Test void examples() {
        assertTrue(s.isHappy(19));
        assertFalse(s.isHappy(2));
        assertTrue(s.isHappy(1));
        assertTrue(s.isHappy(7));
    }
}
```
