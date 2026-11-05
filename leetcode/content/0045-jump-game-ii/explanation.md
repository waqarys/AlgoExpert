# 0045. Jump Game II

**Difficulty:** Medium | **Category:** Greedy | **LeetCode:** https://leetcode.com/problems/jump-game-ii/

## Problem
- Return the minimum number of jumps to reach the last index (always reachable).

## Intuition
- Implicit BFS: all indices reachable with j jumps form a contiguous window. The next window ends at the farthest point reachable from the current window.

## Brute Force
- DP: dp[i] = min over j < i reaching i of dp[j] + 1: O(n^2).

## Optimal Approach
1. jumps = 0, end = 0 (current window end), far = 0.
2. For i in 0..n-2: far = max(far, i + nums[i]); if i == end: jumps++, end = far.

## Worked Example
- [2,3,1,1,4].
```text
i=0 far=2 i==end(0) -> jumps=1 end=2
i=1 far=4
i=2 far=4 i==end(2) -> jumps=2 end=4
answer 2
```

## Complexity
- Time: O(n). Space: O(1).

## Pitfalls
- Loop to n-2: jumping from the last index would count an extra jump.

## Video Script
- Draw the windows as BFS levels over an array.

## Solution
```java file=greedy/JumpGameII.java
package greedy;

/**
 * LC 45 Jump Game II.
 * Approach: greedy BFS over windows of indices reachable with the same jump count.
 * Time O(n), Space O(1).
 */
public class JumpGameII {
    public int jump(int[] nums) {
        int jumps = 0, end = 0, far = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            far = Math.max(far, i + nums[i]);
            if (i == end) { jumps++; end = far; }
        }
        return jumps;
    }
}
```

## Tests
```java test=greedy/JumpGameIITest.java
package greedy;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class JumpGameIITest {
    JumpGameII s = new JumpGameII();
    @Test void examples() {
        assertEquals(2, s.jump(new int[]{2, 3, 1, 1, 4}));
        assertEquals(2, s.jump(new int[]{2, 3, 0, 1, 4}));
        assertEquals(0, s.jump(new int[]{0}));
        assertEquals(1, s.jump(new int[]{5, 1, 1}));
    }
}
```
