# 0567. Permutation in String

**Difficulty:** Medium | **Category:** Sliding Window | **LeetCode:** https://leetcode.com/problems/permutation-in-string/

## Problem
- Return true if some permutation of s1 is a substring of s2.
- Example: s1 = "ab", s2 = "eidbaooo" -> true ("ba").

## Intuition
- A permutation of s1 is any window of length |s1| with identical letter counts.
- Slide a fixed-size window over s2 and keep a count of how many of the 26 letters currently match.

## Brute Force
- For every window, compare 26 counts: O(26 * n). Fine too, but the "matches" counter makes each step O(1).

## Optimal Approach
1. need[26] from s1, have[26] for the window.
2. matches = number of letters where need == have.
3. When a char enters/leaves, update have and adjust matches only for that letter.
4. If matches == 26, return true.

## Worked Example
- s1 = "ab", s2 = "eidbaooo".
```text
window "ei" -> no
window "id" -> no
window "db" -> no
window "ba" -> counts a1 b1 match need -> true
```

## Complexity
- Time: O(|s1| + |s2|). Space: O(26).

## Pitfalls
- If |s1| > |s2| return false immediately.

## Video Script
- Contrast fixed-size windows (this) with variable windows (problem 3). Explain the matches counter.

## Solution
```java file=slidingwindow/PermutationInString.java
package slidingwindow;

/**
 * LC 567 Permutation in String.
 * Approach: fixed-size window over s2 with letter counts; compare to s1's counts.
 * Time O(n), Space O(1).
 */
public class PermutationInString {
    public boolean checkInclusion(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        if (m > n) return false;
        int[] diff = new int[26]; // need - have
        for (int i = 0; i < m; i++) {
            diff[s1.charAt(i) - 'a']++;
            diff[s2.charAt(i) - 'a']--;
        }
        int zeros = 0;
        for (int d : diff) if (d == 0) zeros++;
        if (zeros == 26) return true;
        for (int r = m; r < n; r++) {
            zeros = update(diff, s2.charAt(r) - 'a', -1, zeros);
            zeros = update(diff, s2.charAt(r - m) - 'a', +1, zeros);
            if (zeros == 26) return true;
        }
        return false;
    }

    private int update(int[] diff, int c, int delta, int zeros) {
        if (diff[c] == 0) zeros--;
        diff[c] += delta;
        if (diff[c] == 0) zeros++;
        return zeros;
    }
}
```

## Tests
```java test=slidingwindow/PermutationInStringTest.java
package slidingwindow;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class PermutationInStringTest {
    PermutationInString s = new PermutationInString();
    @Test void examples() {
        assertTrue(s.checkInclusion("ab", "eidbaooo"));
        assertFalse(s.checkInclusion("ab", "eidboaoo"));
    }
    @Test void edges() {
        assertFalse(s.checkInclusion("abc", "ab"));
        assertTrue(s.checkInclusion("adc", "dcda"));
        assertTrue(s.checkInclusion("a", "a"));
    }
}
```
