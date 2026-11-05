# 0136. Single Number

**Difficulty:** Easy | **Category:** Bit Manipulation | **LeetCode:** https://leetcode.com/problems/single-number/

## Problem
- Every element appears twice except one. Find it in O(n) time and O(1) space.

## Intuition
- XOR is its own inverse (a ^ a = 0) and order does not matter, so XOR-ing everything cancels the pairs and leaves the single value.

## Brute Force
- HashSet add/remove: O(n) space.

## Optimal Approach
1. x = 0; for each v: x ^= v. Return x.

## Worked Example
- [4,1,2,1,2].
```text
0^4=4  4^1=5  5^2=7  7^1=6  6^2=4  -> 4
```

## Complexity
- Time: O(n). Space: O(1).

## Pitfalls
- Works for negatives too, because XOR is bitwise.

## Video Script
- Introduce the three XOR identities: a^0 = a, a^a = 0, and order does not matter.

## Solution
```java file=bits/SingleNumber.java
package bits;

/**
 * LC 136 Single Number.
 * Approach: XOR all values; pairs cancel.
 * Time O(n), Space O(1).
 */
public class SingleNumber {
    public int singleNumber(int[] nums) {
        int x = 0;
        for (int v : nums) x ^= v;
        return x;
    }
}
```

## Tests
```java test=bits/SingleNumberTest.java
package bits;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SingleNumberTest {
    SingleNumber s = new SingleNumber();
    @Test void examples() {
        assertEquals(1, s.singleNumber(new int[]{2, 2, 1}));
        assertEquals(4, s.singleNumber(new int[]{4, 1, 2, 1, 2}));
        assertEquals(-7, s.singleNumber(new int[]{-7}));
    }
}
```
