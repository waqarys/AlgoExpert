# 0853. Car Fleet

**Difficulty:** Medium | **Category:** Stack | **LeetCode:** https://leetcode.com/problems/car-fleet/

## Problem
- Cars at position[i] with speed[i] drive toward target. A faster car that catches a slower one ahead joins it as a fleet (moving at the slower speed). How many fleets arrive?
- Example: target 12, position [10,8,0,5,3], speed [2,4,1,1,3] -> 3.

## Intuition
- Compute each car's arrival time if it were alone: (target - pos) / speed.
- Process cars from closest to target backwards. A car behind with time <= the fleet ahead catches it and merges; a larger time starts a new fleet.

## Brute Force
- Simulate time steps: slow, and floating-point merges get messy.

## Optimal Approach
1. Sort cars by position descending.
2. Keep the time of the last fleet; for each car t = (target-p)/s.
3. If t > lastFleetTime, it is a new fleet: count++, lastFleetTime = t.

## Worked Example
- target 12.
```text
pos 10 speed 2 -> t=1    new fleet (1)
pos  8 speed 4 -> t=1    <=1 merges
pos  5 speed 1 -> t=7    new fleet (2)
pos  3 speed 3 -> t=3    <=7 merges
pos  0 speed 1 -> t=12   new fleet (3)
```

## Complexity
- Time: O(n log n) for sorting. Space: O(n).

## Pitfalls
- Use double for the time; integer division gives wrong merges.
- Catching exactly at the target still counts as one fleet (<=).

## Video Script
- Reframe from positions to arrival times; the "stack" is just the slowest time ahead.

## Solution
```java file=stack/CarFleet.java
package stack;

import java.util.*;

/**
 * LC 853 Car Fleet.
 * Approach: sort by position desc; a car whose solo arrival time exceeds the fleet ahead starts a new fleet.
 * Time O(n log n), Space O(n).
 */
public class CarFleet {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> position[b] - position[a]);
        int fleets = 0;
        double last = -1;
        for (int i : idx) {
            double t = (double) (target - position[i]) / speed[i];
            if (t > last) { fleets++; last = t; }
        }
        return fleets;
    }
}
```

## Tests
```java test=stack/CarFleetTest.java
package stack;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CarFleetTest {
    CarFleet s = new CarFleet();
    @Test void examples() {
        assertEquals(3, s.carFleet(12, new int[]{10, 8, 0, 5, 3}, new int[]{2, 4, 1, 1, 3}));
        assertEquals(1, s.carFleet(10, new int[]{3}, new int[]{3}));
        assertEquals(1, s.carFleet(100, new int[]{0, 2, 4}, new int[]{4, 2, 1}));
        assertEquals(2, s.carFleet(10, new int[]{6, 8}, new int[]{3, 2}));
    }
}
```
