# 0746. Min Cost Climbing Stairs

**Difficulty:** Easy | **Category:** 1-D Dynamic Programming | **LeetCode:** https://leetcode.com/problems/min-cost-climbing-stairs/

## Problem
- cost[i] is paid when you step on stair i; you may then climb 1 or 2. Start at index 0 or 1. Return the minimum cost to reach the top (index n).

## Intuition
- dp[i] = minimum cost to stand on i (before paying for it) = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]).

## Brute Force
- Recursion over both choices: O(2^n).

## Optimal Approach
1. a = dp[0] = 0, b = dp[1] = 0.
2. For i = 2..n: c = min(b + cost[i-1], a + cost[i-2]); shift.
3. Return b.

## Worked Example
- cost = [10,15,20].
```text
dp[0]=0 dp[1]=0
dp[2]=min(0+15, 0+10)=10
dp[3]=min(10+20, 0+15)=15   -> answer 15
```

## Complexity
- Time: O(n). Space: O(1).

## Pitfalls
- The top is index n (past the last stair).

## Video Script
- Same skeleton as problem 70, now minimising instead of counting.

## Solution
```java file=dp1/MinCostClimbingStairs.java
package dp1;

/**
 * LC 746 Min Cost Climbing Stairs.
 * Approach: dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]) rolled into two variables.
 * Time O(n), Space O(1).
 */
public class MinCostClimbingStairs {
    public int minCostClimbingStairs(int[] cost) {
        int a = 0, b = 0;
        for (int i = 2; i <= cost.length; i++) {
            int c = Math.min(b + cost[i - 1], a + cost[i - 2]);
            a = b;
            b = c;
        }
        return b;
    }
}
```

## Tests
```java test=dp1/MinCostClimbingStairsTest.java
package dp1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MinCostClimbingStairsTest {
    MinCostClimbingStairs s = new MinCostClimbingStairs();
    @Test void examples() {
        assertEquals(15, s.minCostClimbingStairs(new int[]{10, 15, 20}));
        assertEquals(6, s.minCostClimbingStairs(new int[]{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}));
        assertEquals(0, s.minCostClimbingStairs(new int[]{5, 0}));
    }
}
```
