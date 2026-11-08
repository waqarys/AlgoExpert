# 0055. Jump Game

**Difficulty:** Medium | **Category:** Greedy | **LeetCode:** https://leetcode.com/problems/jump-game/

## Problem
- nums[i] is the maximum jump length from i. Starting at index 0, can you reach the last index?

## Intuition
- Track the farthest index reachable so far. If the current index is beyond it, we are stuck.

## Brute Force
- DP/DFS over every jump: O(n^2).

## Optimal Approach
1. reach = 0.
2. For i: if i > reach return false; reach = max(reach, i + nums[i]).
3. Return true.

## Worked Example
- [3,2,1,0,4].
```text
i=0 reach=3
i=1 reach=3
i=2 reach=3
i=3 reach=3
i=4 > reach 3 -> false
```

## Complexity
- Time: O(n). Space: O(1).

## Pitfalls
- Early exit once reach >= n-1 is an optional speed-up.

## Video Script
- "How far can I get?" - one variable replaces a whole DP table.

## Solution
```java file=greedy/JumpGame.java
package greedy;

/**
 * LC 55 Jump Game.
 * Approach: greedy farthest-reach scan.
 * Time O(n), Space O(1).
 */
public class JumpGame {
    public boolean canJump(int[] nums) {
        int reach = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > reach) return false;
            reach = Math.max(reach, i + nums[i]);
        }
        return true;
    }
}
```

## Tests
```java test=greedy/JumpGameTest.java
package greedy;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class JumpGameTest {
    JumpGame s = new JumpGame();
    @Test void examples() {
        assertTrue(s.canJump(new int[]{2, 3, 1, 1, 4}));
        assertFalse(s.canJump(new int[]{3, 2, 1, 0, 4}));
        assertTrue(s.canJump(new int[]{0}));
        assertFalse(s.canJump(new int[]{0, 1}));
    }
}
```
