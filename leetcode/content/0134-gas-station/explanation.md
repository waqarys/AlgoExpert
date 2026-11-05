# 0134. Gas Station

**Difficulty:** Medium | **Category:** Greedy | **LeetCode:** https://leetcode.com/problems/gas-station/

## Problem
- Circular route; gas[i] available at station i, cost[i] to reach i+1. Return the unique start index to complete the circuit, or -1.

## Intuition
- If total gas < total cost, it is impossible.
- Otherwise scan once: whenever the running tank goes negative at i, no station between the current start and i can be a valid start, so move start to i + 1.

## Brute Force
- Simulate from every start: O(n^2).

## Optimal Approach
1. total += gas[i] - cost[i]; tank += gas[i] - cost[i].
2. If tank < 0: start = i + 1, tank = 0.
3. Return total < 0 ? -1 : start.

## Worked Example
- gas [1,2,3,4,5], cost [3,4,5,1,2].
```text
i=0 diff -2 tank -2 -> start=1 tank=0
i=1 diff -2 tank -2 -> start=2
i=2 diff -2 tank -2 -> start=3
i=3 diff +3 tank 3
i=4 diff +3 tank 6
total = 0 >= 0 -> start 3
```

## Complexity
- Time: O(n). Space: O(1).

## Pitfalls
- Why skipping is safe: if start..i fails, any later start in that range begins with less fuel and also fails.

## Video Script
- Visualise the tank level as a line chart; the start is right after its lowest point.

## Solution
```java file=greedy/GasStation.java
package greedy;

/**
 * LC 134 Gas Station.
 * Approach: one pass; reset start after any negative tank; feasible iff total >= 0.
 * Time O(n), Space O(1).
 */
public class GasStation {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int total = 0, tank = 0, start = 0;
        for (int i = 0; i < gas.length; i++) {
            int d = gas[i] - cost[i];
            total += d;
            tank += d;
            if (tank < 0) { start = i + 1; tank = 0; }
        }
        return total < 0 ? -1 : start;
    }
}
```

## Tests
```java test=greedy/GasStationTest.java
package greedy;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class GasStationTest {
    GasStation s = new GasStation();
    @Test void examples() {
        assertEquals(3, s.canCompleteCircuit(new int[]{1, 2, 3, 4, 5}, new int[]{3, 4, 5, 1, 2}));
        assertEquals(-1, s.canCompleteCircuit(new int[]{2, 3, 4}, new int[]{3, 4, 3}));
        assertEquals(0, s.canCompleteCircuit(new int[]{5}, new int[]{4}));
    }
}
```
