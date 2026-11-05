# 0150. Evaluate Reverse Polish Notation

**Difficulty:** Medium | **Category:** Stack | **LeetCode:** https://leetcode.com/problems/evaluate-reverse-polish-notation/

## Problem
- Evaluate a postfix expression given as tokens (+, -, *, / and integers). Division truncates toward zero.
- Example: ["2","1","+","3","*"] -> 9.

## Intuition
- In postfix, an operator applies to the two most recent values, so a stack of operands is all we need.

## Brute Force
- Repeatedly find the first operator and collapse it with its two predecessors: O(n^2).

## Optimal Approach
1. Number: push it.
2. Operator: b = pop, a = pop (order matters!), push a op b.
3. Result is the single remaining value.

## Worked Example
- ["4","13","5","/","+"].
```text
4      [4]
13     [4,13]
5      [4,13,5]
/      13/5=2   [4,2]
+      4+2=6    [6]
```

## Complexity
- Time: O(n). Space: O(n).

## Pitfalls
- Operand order for - and /: the second pop is the left operand.
- "-3" is a number, not an operator; compare the whole token.

## Video Script
- Explain postfix as "calculator without parentheses", then animate the stack.

## Solution
```java file=stack/EvaluateReversePolishNotation.java
package stack;

import java.util.*;

/**
 * LC 150 Evaluate Reverse Polish Notation.
 * Approach: operand stack; on an operator pop b then a and push a op b.
 * Time O(n), Space O(n).
 */
public class EvaluateReversePolishNotation {
    public int evalRPN(String[] tokens) {
        Deque<Integer> st = new ArrayDeque<>();
        for (String t : tokens) {
            switch (t) {
                case "+" -> st.push(st.pop() + st.pop());
                case "*" -> st.push(st.pop() * st.pop());
                case "-" -> { int b = st.pop(), a = st.pop(); st.push(a - b); }
                case "/" -> { int b = st.pop(), a = st.pop(); st.push(a / b); }
                default -> st.push(Integer.parseInt(t));
            }
        }
        return st.pop();
    }
}
```

## Tests
```java test=stack/EvaluateReversePolishNotationTest.java
package stack;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class EvaluateReversePolishNotationTest {
    EvaluateReversePolishNotation s = new EvaluateReversePolishNotation();
    @Test void examples() {
        assertEquals(9, s.evalRPN(new String[]{"2", "1", "+", "3", "*"}));
        assertEquals(6, s.evalRPN(new String[]{"4", "13", "5", "/", "+"}));
        assertEquals(22, s.evalRPN(new String[]{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}));
    }
    @Test void truncation() { assertEquals(-2, s.evalRPN(new String[]{"-7", "3", "/"})); }
}
```
