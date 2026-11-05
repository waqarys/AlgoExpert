# 0739. Daily Temperatures

**Difficulty:** Medium | **Category:** Stack | **LeetCode:** https://leetcode.com/problems/daily-temperatures/

## Problem
- For each day, how many days until a warmer temperature? 0 if never.
- Example: [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0].

## Intuition
- Keep a stack of days still waiting for a warmer day; their temperatures are decreasing from bottom to top.
- A new warmer day resolves every waiting day on top that is colder than it.

## Brute Force
- For each day scan forward: O(n^2).

## Optimal Approach
1. For i: while stack non-empty and T[i] > T[top]: j = pop, ans[j] = i - j.
2. Push i.

## Worked Example
- [73,74,75,71,69,72,76,73].
```text
i=0 73 push            st=[0]
i=1 74 pop 0 ans=1     st=[1]
i=2 75 pop 1 ans=1     st=[2]
i=3 71 push            st=[2,3]
i=4 69 push            st=[2,3,4]
i=5 72 pop 4(1) pop 3(2)  st=[2,5]
i=6 76 pop 5(1) pop 2(4)  st=[6]
i=7 73 push            st=[6,7]  -> leftovers stay 0
```

## Complexity
- Time: O(n), each index pushed/popped once. Space: O(n).

## Pitfalls
- Strictly warmer: use >, not >=.

## Video Script
- Introduce the monotonic stack: "next greater element" template.

## Solution
```java file=stack/DailyTemperatures.java
package stack;

import java.util.*;

/**
 * LC 739 Daily Temperatures.
 * Approach: monotonic decreasing stack of indices waiting for a warmer day.
 * Time O(n), Space O(n).
 */
public class DailyTemperatures {
    public int[] dailyTemperatures(int[] t) {
        int[] ans = new int[t.length];
        Deque<Integer> st = new ArrayDeque<>();
        for (int i = 0; i < t.length; i++) {
            while (!st.isEmpty() && t[i] > t[st.peek()]) {
                int j = st.pop();
                ans[j] = i - j;
            }
            st.push(i);
        }
        return ans;
    }
}
```

## Tests
```java test=stack/DailyTemperaturesTest.java
package stack;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class DailyTemperaturesTest {
    DailyTemperatures s = new DailyTemperatures();
    @Test void examples() {
        assertArrayEquals(new int[]{1, 1, 4, 2, 1, 1, 0, 0}, s.dailyTemperatures(new int[]{73, 74, 75, 71, 69, 72, 76, 73}));
        assertArrayEquals(new int[]{1, 1, 1, 0}, s.dailyTemperatures(new int[]{30, 40, 50, 60}));
        assertArrayEquals(new int[]{0, 0, 0}, s.dailyTemperatures(new int[]{50, 50, 50}));
    }
}
```
