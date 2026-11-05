# 0020. Valid Parentheses

**Difficulty:** Easy | **Category:** Stack | **LeetCode:** https://leetcode.com/problems/valid-parentheses/

## Problem
- s contains only ()[]{}. It is valid if every opener is closed by the same type in the correct order.
- Example: "()[]{}" -> true, "(]" -> false, "([)]" -> false.

## Intuition
- The most recent unclosed opener must be closed first: last in, first out, so use a stack.
- Trick: push the expected closer instead of the opener, then a closer just has to equal the popped value.

## Brute Force
- Repeatedly delete "()", "[]", "{}" until nothing changes: O(n^2).

## Optimal Approach
1. For each char: if it is an opener, push its matching closer.
2. Else if the stack is empty or pop() != char, return false.
3. At the end, return stack.isEmpty().

## Worked Example
- s = "([)]".
```text
'(' push ')'   stack=[)]
'[' push ']'   stack=[),]]
')' pop ']'    ']' != ')' -> false
```

## Complexity
- Time: O(n). Space: O(n).

## Pitfalls
- Leftover openers ("((") mean invalid, so check emptiness at the end.
- A closer on an empty stack ("]") is invalid.

## Video Script
- Show nesting as "last opened, first closed"; that sentence is the definition of a stack.

## Solution
```java file=stack/ValidParentheses.java
package stack;

import java.util.*;

/**
 * LC 20 Valid Parentheses.
 * Approach: stack of expected closers; each closer must match the top.
 * Time O(n), Space O(n).
 */
public class ValidParentheses {
    public boolean isValid(String s) {
        Deque<Character> st = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (c == '(') st.push(')');
            else if (c == '[') st.push(']');
            else if (c == '{') st.push('}');
            else if (st.isEmpty() || st.pop() != c) return false;
        }
        return st.isEmpty();
    }
}
```

## Tests
```java test=stack/ValidParenthesesTest.java
package stack;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ValidParenthesesTest {
    ValidParentheses s = new ValidParentheses();
    @Test void examples() {
        assertTrue(s.isValid("()[]{}"));
        assertFalse(s.isValid("(]"));
        assertFalse(s.isValid("([)]"));
        assertTrue(s.isValid("{[]}"));
    }
    @Test void edges() { assertFalse(s.isValid("((")); assertFalse(s.isValid("]")); assertTrue(s.isValid("")); }
}
```
