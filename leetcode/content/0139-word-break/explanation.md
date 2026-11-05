# 0139. Word Break

**Difficulty:** Medium | **Category:** 1-D Dynamic Programming | **LeetCode:** https://leetcode.com/problems/word-break/

## Problem
- Can s be segmented into a sequence of dictionary words (reuse allowed)?

## Intuition
- dp[i] = true if the prefix s[0..i) can be segmented. It is true if some j < i has dp[j] true and s[j..i) is a word.

## Brute Force
- Recursion trying every split: exponential without memo.

## Optimal Approach
1. dp[0] = true; dict as a set; maxLen = longest word.
2. For i = 1..n, for j from i-1 down to max(0, i - maxLen): if dp[j] and dict has s[j..i), dp[i] = true; break.

## Worked Example
- s = "leetcode", dict [leet, code].
```text
dp[0]=T
dp[4]: s[0..4)="leet" in dict, dp[0]=T -> T
dp[8]: s[4..8)="code" in dict, dp[4]=T -> T
answer true
```

## Complexity
- Time: O(n * maxLen * maxLen) with substring hashing. Space: O(n).

## Pitfalls
- Bounding j by the longest word length avoids pointless substring checks.

## Video Script
- Draw cut points under the string; dp[i] lights up when a word ends there.

## Solution
```java file=dp1/WordBreak.java
package dp1;

import java.util.*;

/**
 * LC 139 Word Break.
 * Approach: dp[i] = some j with dp[j] && s[j..i) in dict; j limited by the longest word.
 * Time O(n * L^2), Space O(n).
 */
public class WordBreak {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> dict = new HashSet<>(wordDict);
        int maxLen = 0;
        for (String w : wordDict) maxLen = Math.max(maxLen, w.length());
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        for (int i = 1; i <= s.length(); i++)
            for (int j = i - 1; j >= Math.max(0, i - maxLen); j--)
                if (dp[j] && dict.contains(s.substring(j, i))) { dp[i] = true; break; }
        return dp[s.length()];
    }
}
```

## Tests
```java test=dp1/WordBreakTest.java
package dp1;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class WordBreakTest {
    WordBreak s = new WordBreak();
    @Test void examples() {
        assertTrue(s.wordBreak("leetcode", List.of("leet", "code")));
        assertTrue(s.wordBreak("applepenapple", List.of("apple", "pen")));
        assertFalse(s.wordBreak("catsandog", List.of("cats", "dog", "sand", "and", "cat")));
    }
}
```
