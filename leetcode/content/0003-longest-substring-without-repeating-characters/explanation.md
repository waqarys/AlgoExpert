# 0003. Longest Substring Without Repeating Characters

**Difficulty:** Medium | **Category:** Sliding Window | **LeetCode:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Problem
- Return the length of the longest substring of s with all distinct characters.
- Example: "abcabcbb" -> 3 ("abc"); "pwwkew" -> 3 ("wke").

## Intuition
- Keep a window [l, r] with no repeats. When s[r] is already inside the window, jump l just past its previous occurrence.
- Remembering the last index of each character lets l jump in O(1).

## Brute Force
- Check every substring for uniqueness: O(n^3), or O(n^2) with a set per start.

## Optimal Approach
1. last[c] = last index of c (initially -1); l = 0.
2. For r: if last[s[r]] >= l, set l = last[s[r]] + 1.
3. last[s[r]] = r; best = max(best, r - l + 1).

## Worked Example
- s = "abba".
```text
r=0 a  l=0  last a=0  len 1
r=1 b  l=0  last b=1  len 2
r=2 b  seen at 1>=0 -> l=2  len 1
r=3 a  seen at 0 < l=2 -> keep l=2  len 2
best = 2
```

## Complexity
- Time: O(n). Space: O(charset), 128 for ASCII.

## Pitfalls
- l must never move backwards ("abba" case) - only jump when the old index is inside the window.

## Video Script
- Introduce the variable-size sliding window template: expand right, shrink left when the invariant breaks.

## Solution
```java file=slidingwindow/LongestSubstringWithoutRepeating.java
package slidingwindow;

import java.util.*;

/**
 * LC 3 Longest Substring Without Repeating Characters.
 * Approach: sliding window; last-seen index lets the left edge jump past a repeat.
 * Time O(n), Space O(charset).
 */
public class LongestSubstringWithoutRepeating {
    public int lengthOfLongestSubstring(String s) {
        int[] last = new int[128];
        Arrays.fill(last, -1);
        int l = 0, best = 0;
        for (int r = 0; r < s.length(); r++) {
            char c = s.charAt(r);
            if (last[c] >= l) l = last[c] + 1;
            last[c] = r;
            best = Math.max(best, r - l + 1);
        }
        return best;
    }
}
```

## Tests
```java test=slidingwindow/LongestSubstringWithoutRepeatingTest.java
package slidingwindow;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LongestSubstringWithoutRepeatingTest {
    LongestSubstringWithoutRepeating s = new LongestSubstringWithoutRepeating();
    @Test void examples() {
        assertEquals(3, s.lengthOfLongestSubstring("abcabcbb"));
        assertEquals(1, s.lengthOfLongestSubstring("bbbbb"));
        assertEquals(3, s.lengthOfLongestSubstring("pwwkew"));
    }
    @Test void edges() {
        assertEquals(0, s.lengthOfLongestSubstring(""));
        assertEquals(2, s.lengthOfLongestSubstring("abba"));
        assertEquals(3, s.lengthOfLongestSubstring("a b"));
    }
}
```
