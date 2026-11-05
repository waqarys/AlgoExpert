# 0125. Valid Palindrome

**Difficulty:** Easy | **Category:** Two Pointers | **LeetCode:** https://leetcode.com/problems/valid-palindrome/

## Problem
- After lowercasing and dropping non-alphanumeric characters, does the string read the same forwards and backwards?
- Example: "A man, a plan, a canal: Panama" -> true; "race a car" -> false.

## Intuition
- A palindrome mirrors around its centre, so compare the outermost valid characters and move inward.
- Skipping junk characters in place avoids building a cleaned copy.

## Brute Force
- Build a filtered lowercase string, reverse it, compare: O(n) time but O(n) extra space.

## Optimal Approach
1. l = 0, r = n-1.
2. Move l right while s[l] is not alphanumeric; move r left likewise.
3. If lower(s[l]) != lower(s[r]) return false; else l++, r--.
4. Return true when the pointers cross.

## Worked Example
- s = "race a car".
```text
l=r(0) r=r(9)   r==r ok
l=a(1) r=a(8)   ok
l=c(2) r=c(7)   ok
l=e(3) r=' '(6) skip -> r=a(5)   e != a -> false
```

## Complexity
- Time: O(n). Space: O(1).

## Pitfalls
- Digits count as alphanumeric ("0P" is false).
- Inner skip loops must also check l < r.

## Video Script
- Show the "clean and reverse" answer, then upgrade to two pointers with in-place skipping.

## Solution
```java file=twopointers/ValidPalindrome.java
package twopointers;

/**
 * LC 125 Valid Palindrome.
 * Approach: two pointers from both ends, skipping non-alphanumerics, comparing case-insensitively.
 * Time O(n), Space O(1).
 */
public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            while (l < r && !Character.isLetterOrDigit(s.charAt(l))) l++;
            while (l < r && !Character.isLetterOrDigit(s.charAt(r))) r--;
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) return false;
            l++;
            r--;
        }
        return true;
    }
}
```

## Tests
```java test=twopointers/ValidPalindromeTest.java
package twopointers;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ValidPalindromeTest {
    ValidPalindrome s = new ValidPalindrome();
    @Test void examples() {
        assertTrue(s.isPalindrome("A man, a plan, a canal: Panama"));
        assertFalse(s.isPalindrome("race a car"));
        assertTrue(s.isPalindrome(" "));
    }
    @Test void digits() { assertFalse(s.isPalindrome("0P")); assertTrue(s.isPalindrome("1a1")); }
}
```
