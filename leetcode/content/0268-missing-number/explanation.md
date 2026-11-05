# 0268. Missing Number

**Difficulty:** Easy | **Category:** Bit Manipulation | **LeetCode:** https://leetcode.com/problems/missing-number/

## Problem
- nums holds n distinct numbers from 0..n. Return the one that is missing.

## Intuition
- XOR all indices 0..n with all values; every present number cancels with its index, leaving the missing one.
- The sum formula n(n+1)/2 - sum also works.

## Brute Force
- Sort and scan (O(n log n)), or use a HashSet (O(n) space).

## Optimal Approach
1. x = n.
2. For each i: x ^= i ^ nums[i].
3. Return x.

## Worked Example
- [3,0,1], n = 3.
```text
x = 3
i=0: x ^= 0 ^ 3 -> 0
i=1: x ^= 1 ^ 0 -> 1
i=2: x ^= 2 ^ 1 -> 2
answer 2
```

## Complexity
- Time: O(n). Space: O(1).

## Pitfalls
- Start x at n, because the loop never visits index n.

## Video Script
- Pair this with Single Number: the same XOR cancellation idea.

## Solution
```java file=bits/MissingNumber.java
package bits;

/**
 * LC 268 Missing Number.
 * Approach: XOR all indices and values; the unmatched number remains.
 * Time O(n), Space O(1).
 */
public class MissingNumber {
    public int missingNumber(int[] nums) {
        int x = nums.length;
        for (int i = 0; i < nums.length; i++) x ^= i ^ nums[i];
        return x;
    }
}
```

## Tests
```java test=bits/MissingNumberTest.java
package bits;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MissingNumberTest {
    MissingNumber s = new MissingNumber();
    @Test void examples() {
        assertEquals(2, s.missingNumber(new int[]{3, 0, 1}));
        assertEquals(2, s.missingNumber(new int[]{0, 1}));
        assertEquals(8, s.missingNumber(new int[]{9, 6, 4, 2, 3, 5, 7, 0, 1}));
        assertEquals(0, s.missingNumber(new int[]{1}));
    }
}
```
