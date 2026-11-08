# 0647. Palindromic Substrings

**Difficulty:** Medium | **Category:** 1-D Dynamic Programming | **LeetCode:** https://leetcode.com/problems/palindromic-substrings/

## Problem
- Count the palindromic substrings of s (different positions count separately).

## Intuition
- Same centre expansion as problem 5, but count every successful expansion step.

## Brute Force
- Check all substrings: O(n^3).

## Optimal Approach
1. For every centre (i, i) and (i, i+1): while ends match, count++ and expand.

## Worked Example
- "aaa".
```text
odd centres : a | a, aaa | a          -> 4
even centres: aa | aa                 -> 2
total 6
```

## Complexity
- Time: O(n^2). Space: O(1).

## Pitfalls
- Single characters count.

## Video Script
- Film right after problem 5; change one line.

## Solution
```java file=dp1/PalindromicSubstrings.java
package dp1;

/**
 * LC 647 Palindromic Substrings.
 * Approach: expand around every centre, counting each palindrome found.
 * Time O(n^2), Space O(1).
 */
public class PalindromicSubstrings {
    public int countSubstrings(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) count += expand(s, i, i) + expand(s, i, i + 1);
        return count;
    }

    private int expand(String s, int l, int r) {
        int c = 0;
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) { c++; l--; r++; }
        return c;
    }
}
```

## Tests
```java test=dp1/PalindromicSubstringsTest.java
package dp1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class PalindromicSubstringsTest {
    PalindromicSubstrings s = new PalindromicSubstrings();
    @Test void examples() {
        assertEquals(3, s.countSubstrings("abc"));
        assertEquals(6, s.countSubstrings("aaa"));
        assertEquals(1, s.countSubstrings("x"));
    }
}
```
