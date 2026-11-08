# 0010. Regular Expression Matching

**Difficulty:** Hard | **Category:** 2-D Dynamic Programming | **LeetCode:** https://leetcode.com/problems/regular-expression-matching/

## Problem
- Implement full-string matching with '.' (any single char) and '*' (zero or more of the preceding element).

## Intuition
- dp[i][j] = does s[0..i) match p[0..j)?
- If p[j-1] is '*': either use zero copies (dp[i][j-2]) or, if s[i-1] matches p[j-2], consume one char of s (dp[i-1][j]).
- Otherwise: chars match (or '.') and dp[i-1][j-1].

## Brute Force
- Plain recursion on the two branches of '*': exponential.

## Optimal Approach
1. dp[0][0] = true; dp[0][j] = p[j-1] == '*' && dp[0][j-2] (patterns like a*b* match empty).
2. Fill the table with the rules above.

## Worked Example
- s = "aab", p = "c*a*b".
```text
"c*" matches empty (zero c's)
"a*" consumes "aa"
"b" matches "b"
dp[3][5] = true
```

## Complexity
- Time: O(m * n). Space: O(m * n).

## Pitfalls
- '*' applies to the previous element, so look at p[j-2].
- Matching must cover the whole string, not a substring.

## Video Script
- Build the table cell by cell for "aa" vs "a*" to show how '*' rows work.

## Solution
```java file=dp2/RegularExpressionMatching.java
package dp2;

/**
 * LC 10 Regular Expression Matching.
 * Approach: 2-D DP over prefixes; '*' = zero copies (j-2) or one more copy (i-1).
 * Time O(mn), Space O(mn).
 */
public class RegularExpressionMatching {
    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[0][0] = true;
        for (int j = 2; j <= n; j++) dp[0][j] = p.charAt(j - 1) == '*' && dp[0][j - 2];
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++) {
                char pc = p.charAt(j - 1);
                if (pc == '*') {
                    dp[i][j] = dp[i][j - 2] || (matches(s.charAt(i - 1), p.charAt(j - 2)) && dp[i - 1][j]);
                } else {
                    dp[i][j] = matches(s.charAt(i - 1), pc) && dp[i - 1][j - 1];
                }
            }
        return dp[m][n];
    }

    private boolean matches(char sc, char pc) { return pc == '.' || pc == sc; }
}
```

## Tests
```java test=dp2/RegularExpressionMatchingTest.java
package dp2;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class RegularExpressionMatchingTest {
    RegularExpressionMatching s = new RegularExpressionMatching();
    @Test void examples() {
        assertFalse(s.isMatch("aa", "a"));
        assertTrue(s.isMatch("aa", "a*"));
        assertTrue(s.isMatch("ab", ".*"));
        assertTrue(s.isMatch("aab", "c*a*b"));
        assertFalse(s.isMatch("mississippi", "mis*is*p*."));
        assertTrue(s.isMatch("", "a*b*"));
    }
}
```
