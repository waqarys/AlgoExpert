# 0155. Min Stack

**Difficulty:** Medium | **Category:** Stack | **LeetCode:** https://leetcode.com/problems/min-stack/

## Problem
- Design a stack with push, pop, top and getMin, each running in O(1).

## Intuition
- The minimum only changes on push/pop, so store "min so far" alongside each element.
- When we pop, the previous minimum is automatically restored from the element below.

## Brute Force
- Scan the stack on getMin: O(n).

## Optimal Approach
1. Each stack entry is a pair (value, minAtThisLevel).
2. push(x): min = empty ? x : min(x, top.min).
3. getMin returns top.min; pop simply removes the pair.

## Worked Example
```text
push -2  -> [(-2,-2)]
push  0  -> [(-2,-2),(0,-2)]
push -3  -> [... ,(-3,-3)]   getMin = -3
pop      -> top=(0,-2)       top = 0, getMin = -2
```

## Complexity
- Time: O(1) for every operation. Space: O(n).

## Pitfalls
- A single "current min" variable fails after popping the min.
- A two-stack variant (push to minStack only when x <= min) must use <= to handle duplicates.

## Video Script
- Show why one variable breaks, then "every level remembers its own min".

## Solution
```java file=stack/MinStack.java
package stack;

import java.util.*;

/**
 * LC 155 Min Stack.
 * Approach: each entry stores {value, min of the stack up to this entry}.
 * Time O(1) per op, Space O(n).
 */
public class MinStack {
    private final Deque<int[]> st = new ArrayDeque<>();

    public void push(int val) {
        int min = st.isEmpty() ? val : Math.min(val, st.peek()[1]);
        st.push(new int[]{val, min});
    }

    public void pop() { st.pop(); }

    public int top() { return st.peek()[0]; }

    public int getMin() { return st.peek()[1]; }
}
```

## Tests
```java test=stack/MinStackTest.java
package stack;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MinStackTest {
    @Test void example() {
        MinStack m = new MinStack();
        m.push(-2); m.push(0); m.push(-3);
        assertEquals(-3, m.getMin());
        m.pop();
        assertEquals(0, m.top());
        assertEquals(-2, m.getMin());
    }
    @Test void duplicateMins() {
        MinStack m = new MinStack();
        m.push(1); m.push(1); m.pop();
        assertEquals(1, m.getMin());
    }
}
```
