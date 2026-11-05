# 0066. Plus One

**Difficulty:** Easy | **Category:** Math & Geometry | **LeetCode:** https://leetcode.com/problems/plus-one/

## Problem
- A number is stored as an array of digits, most significant first. Add one.

## Intuition
- Walk from the last digit: a digit below 9 just increments and we are done; a 9 becomes 0 and the carry moves left.
- If every digit was 9, the result is 1 followed by zeros.

## Brute Force
- Convert to a number: overflows for long arrays.

## Optimal Approach
1. For i from the end: if d[i] < 9, d[i]++ and return.
2. Else d[i] = 0.
3. Return a new array of length n+1 with a leading 1.

## Worked Example
- [1,2,9].
```text
i=2: 9 -> 0, carry
i=1: 2 -> 3, return [1,3,0]
```

## Complexity
- Time: O(n). Space: O(1), or O(n) for the all-nines case.

## Pitfalls
- new int[n+1] is zero-filled, so only the first slot needs setting.

## Video Script
- A quick win, good for a Shorts-style video.

## Solution
```java file=math/PlusOne.java
package math;

/**
 * LC 66 Plus One.
 * Approach: propagate the carry from the right; all nines -> new leading 1.
 * Time O(n), Space O(1) (O(n) for all nines).
 */
public class PlusOne {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] < 9) { digits[i]++; return digits; }
            digits[i] = 0;
        }
        int[] res = new int[digits.length + 1];
        res[0] = 1;
        return res;
    }
}
```

## Tests
```java test=math/PlusOneTest.java
package math;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class PlusOneTest {
    PlusOne s = new PlusOne();
    @Test void examples() {
        assertArrayEquals(new int[]{1, 2, 4}, s.plusOne(new int[]{1, 2, 3}));
        assertArrayEquals(new int[]{1, 3, 0}, s.plusOne(new int[]{1, 2, 9}));
        assertArrayEquals(new int[]{1, 0, 0, 0}, s.plusOne(new int[]{9, 9, 9}));
        assertArrayEquals(new int[]{1}, s.plusOne(new int[]{0}));
    }
}
```
