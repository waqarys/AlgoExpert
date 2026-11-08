# 1046. Last Stone Weight

**Difficulty:** Easy | **Category:** Heap / Priority Queue | **LeetCode:** https://leetcode.com/problems/last-stone-weight/

## Problem
- Repeatedly smash the two heaviest stones x <= y: if equal both vanish, else a stone of y - x remains. Return the last weight or 0.

## Intuition
- We always need the two current maxima, so use a max-heap.

## Brute Force
- Sort the array after every smash: O(n^2 log n).

## Optimal Approach
1. Push all stones into a max-heap.
2. While size > 1: y = poll, x = poll; if y != x push y - x.
3. Return heap empty ? 0 : peek.

## Worked Example
- [2,7,4,1,8,1].
```text
8,7 -> 1   heap {4,2,1,1,1}
4,2 -> 2   heap {2,1,1,1}
2,1 -> 1   heap {1,1,1}
1,1 -> 0   heap {1}
answer 1
```

## Complexity
- Time: O(n log n). Space: O(n).

## Pitfalls
- Java PriorityQueue is a min-heap by default; pass Collections.reverseOrder().

## Video Script
- Short warm-up for heaps: simulation with the right data structure.

## Solution
```java file=heap/LastStoneWeight.java
package heap;

import java.util.*;

/**
 * LC 1046 Last Stone Weight.
 * Approach: max-heap simulation.
 * Time O(n log n), Space O(n).
 */
public class LastStoneWeight {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int s : stones) pq.add(s);
        while (pq.size() > 1) {
            int y = pq.poll(), x = pq.poll();
            if (y != x) pq.add(y - x);
        }
        return pq.isEmpty() ? 0 : pq.peek();
    }
}
```

## Tests
```java test=heap/LastStoneWeightTest.java
package heap;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LastStoneWeightTest {
    LastStoneWeight s = new LastStoneWeight();
    @Test void examples() {
        assertEquals(1, s.lastStoneWeight(new int[]{2, 7, 4, 1, 8, 1}));
        assertEquals(1, s.lastStoneWeight(new int[]{1}));
        assertEquals(0, s.lastStoneWeight(new int[]{3, 3}));
    }
}
```
