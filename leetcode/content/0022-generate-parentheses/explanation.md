# 0022. Generate Parentheses

**Difficulty:** Medium | **Category:** Stack | **LeetCode:** https://leetcode.com/problems/generate-parentheses/

## Problem
- Return all well-formed strings of n pairs of parentheses.
- Example: n = 3 -> ["((()))","(()())","(())()","()(())","()()()"].

## Intuition
- Build left to right. We may add "(" while open < n, and ")" only while close < open.
- Those two rules guarantee every completed string is valid, so nothing is generated and then thrown away.

## Brute Force
- Generate all 2^(2n) strings and validate each: O(2^(2n) * n).

## Optimal Approach
1. backtrack(sb, open, close).
2. If length == 2n, record.
3. If open < n: append "(", recurse, remove.
4. If close < open: append ")", recurse, remove.

## Worked Example
- n = 2.
```text
""  -> "("  -> "((" -> "(()" -> "(())"  record
            -> "()" -> "()(" -> "()()"  record
```

## Complexity
- Time: O(4^n / sqrt(n)) (the Catalan number of results, each of length 2n). Space: O(n) recursion.

## Pitfalls
- Undo the append (backtrack) after each branch when using a shared StringBuilder.

## Video Script
- Draw the decision tree and prune it with the two rules.

## Solution
```java file=stack/GenerateParentheses.java
package stack;

import java.util.*;

/**
 * LC 22 Generate Parentheses.
 * Approach: backtracking; add '(' while open < n, ')' while close < open.
 * Time O(Catalan(n) * n), Space O(n).
 */
public class GenerateParentheses {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        go(new StringBuilder(), 0, 0, n, res);
        return res;
    }

    private void go(StringBuilder sb, int open, int close, int n, List<String> res) {
        if (sb.length() == 2 * n) { res.add(sb.toString()); return; }
        if (open < n) { sb.append('('); go(sb, open + 1, close, n, res); sb.deleteCharAt(sb.length() - 1); }
        if (close < open) { sb.append(')'); go(sb, open, close + 1, n, res); sb.deleteCharAt(sb.length() - 1); }
    }
}
```

## Tests
```java test=stack/GenerateParenthesesTest.java
package stack;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class GenerateParenthesesTest {
    GenerateParentheses s = new GenerateParentheses();
    @Test void examples() {
        assertEquals(List.of("((()))", "(()())", "(())()", "()(())", "()()()"), s.generateParenthesis(3));
        assertEquals(List.of("()"), s.generateParenthesis(1));
        assertEquals(14, s.generateParenthesis(4).size());
    }
}
```
