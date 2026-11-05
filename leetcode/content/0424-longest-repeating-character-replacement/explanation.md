# 0424. Longest Repeating Character Replacement

**Difficulty:** Medium | **Category:** Sliding Window | **LeetCode:** https://leetcode.com/problems/longest-repeating-character-replacement/

## Problem
- s has uppercase letters. You may change at most k characters. Return the longest substring that can become all one letter.
- Example: "AABABBA", k = 1 -> 4.

## Intuition
- A window is fixable if (window length - count of its most frequent letter) <= k.
- Grow the window to the right; if it becomes unfixable, slide the left edge by one.
- maxFreq never needs to decrease: a smaller maxFreq could never produce a longer answer than one already recorded.

## Brute Force
- Check every substring with counts: O(26 * n^2).

## Optimal Approach
1. count[26], l = 0, maxFreq = 0.
2. For r: count[s[r]]++, maxFreq = max(maxFreq, count[s[r]]).
3. If (r - l + 1) - maxFreq > k: count[s[l]]--, l++.
4. best = max(best, r - l + 1).

## Worked Example
- s = "AABABBA", k = 1.
```text
r=0 A win=A       maxF=1 ok  best=1
r=1 A win=AA      maxF=2 ok  best=2
r=2 B win=AAB     maxF=2 ok  best=3
r=3 A win=AABA    maxF=3 ok  best=4
r=4 B win=AABAB   5-3=2>1 -> drop A  win=ABAB
r=5 B win=ABABB   5-3=2>1 -> drop A  win=BABB
r=6 A win=BABBA   5-3=2>1 -> drop B  win=ABBA
best = 4
```

## Complexity
- Time: O(n). Space: O(26).

## Pitfalls
- Recomputing the true max on every shrink is correct but O(26n); the stale maxFreq trick is still correct.
- Use if, not while, for the shrink: the window only ever slides, it never needs to shrink by more than one.

## Video Script
- State the fixability formula, then show why the window never has to shrink, it only slides.

## Solution
```java file=slidingwindow/LongestRepeatingCharacterReplacement.java
package slidingwindow;

/**
 * LC 424 Longest Repeating Character Replacement.
 * Approach: sliding window valid while length - maxFreq <= k; slide (not shrink) when invalid.
 * Time O(n), Space O(1).
 */
public class LongestRepeatingCharacterReplacement {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int l = 0, maxFreq = 0, best = 0;
        for (int r = 0; r < s.length(); r++) {
            maxFreq = Math.max(maxFreq, ++count[s.charAt(r) - 'A']);
            if (r - l + 1 - maxFreq > k) count[s.charAt(l++) - 'A']--;
            best = Math.max(best, r - l + 1);
        }
        return best;
    }
}
```

## Tests
```java test=slidingwindow/LongestRepeatingCharacterReplacementTest.java
package slidingwindow;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LongestRepeatingCharacterReplacementTest {
    LongestRepeatingCharacterReplacement s = new LongestRepeatingCharacterReplacement();
    @Test void examples() {
        assertEquals(4, s.characterReplacement("ABAB", 2));
        assertEquals(4, s.characterReplacement("AABABBA", 1));
    }
    @Test void edges() {
        assertEquals(1, s.characterReplacement("A", 0));
        assertEquals(2, s.characterReplacement("ABCD", 1));
        assertEquals(5, s.characterReplacement("AAAAA", 0));
    }
}
```
