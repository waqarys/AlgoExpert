# 0242. Valid Anagram

**Difficulty:** Easy | **Category:** Arrays & Hashing | **LeetCode:** https://leetcode.com/problems/valid-anagram/

## Problem
- Given strings s and t, return true if t is a rearrangement of the letters of s.
- Example: s = "anagram", t = "nagaram" -> true; s = "rat", t = "car" -> false.

## Intuition
- Two strings are anagrams exactly when every character occurs the same number of times in both.
- With only lowercase letters, a 26-slot count array is a perfect, tiny hash map.

## Brute Force
- Sort both strings and compare: O(n log n) time.

## Optimal Approach
1. If lengths differ, return false immediately.
2. For each index i: count[s[i]]++ and count[t[i]]--.
3. If every count is zero at the end, the multisets match.

## Worked Example
- s = "rat", t = "car".
```text
i=0  +r -c   r:1 c:-1
i=1  +a -a   a:0
i=2  +t -r   t:1 r:0
counts not all zero (c=-1, t=1) -> false
```

## Complexity
- Time: O(n).
- Space: O(1), the array always has 26 slots. For Unicode use a HashMap (O(k) distinct chars).

## Pitfalls
- Forgetting the length check makes "a" vs "ab" look valid if you only scan s.
- For the Unicode follow-up, iterate code points, not chars.

## Video Script
- Define anagram as "same letter counts". Show sorting as the obvious answer.
- Then show the counting trick with one array: increment for s, decrement for t.
- Close with the Unicode follow-up and why HashMap generalises.

## Solution
```java file=arrays/ValidAnagram.java
package arrays;

/**
 * LC 242 Valid Anagram. Is t a permutation of s?
 * Approach: 26-letter frequency array, +1 for s and -1 for t, all zeros means anagram.
 * Time O(n), Space O(1).
 */
public class ValidAnagram {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        for (int c : count) if (c != 0) return false;
        return true;
    }
}
```

## Tests
```java test=arrays/ValidAnagramTest.java
package arrays;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ValidAnagramTest {
    ValidAnagram s = new ValidAnagram();
    @Test void examples() {
        assertTrue(s.isAnagram("anagram", "nagaram"));
        assertFalse(s.isAnagram("rat", "car"));
    }
    @Test void edges() {
        assertFalse(s.isAnagram("a", "ab"));
        assertTrue(s.isAnagram("", ""));
        assertFalse(s.isAnagram("aacc", "ccac"));
    }
}
```
