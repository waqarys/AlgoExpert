# 0239. Sliding Window Maximum

**Difficulty:** Hard | **Category:** Sliding Window | **LeetCode:** https://leetcode.com/problems/sliding-window-maximum/

## Problem
- Return the maximum of every window of size k as it slides across nums.
- Example: [1,3,-1,-3,5,3,6,7], k = 3 -> [3,3,5,5,6,7].

## Intuition
- Keep a deque of indices whose values are decreasing from front to back.
- A new value evicts smaller values from the back (they can never be a max again while it exists).
- The front is the current max; drop it when it leaves the window.

## Brute Force
- Scan each window: O(n*k). A max-heap with lazy deletion gives O(n log n).

## Optimal Approach
1. For each i: pop back while nums[back] <= nums[i]; push i.
2. If front <= i - k, pop front.
3. If i >= k-1, output nums[front].

## Worked Example
- nums = [1,3,-1,-3,5,3,6,7], k = 3 (deque shows values).
```text
i=0 1     dq=[1]
i=1 3     dq=[3]
i=2 -1    dq=[3,-1]      out 3
i=3 -3    dq=[3,-1,-3]   out 3
i=4 5     dq=[5]         out 5
i=5 3     dq=[5,3]       out 5
i=6 6     dq=[6]         out 6
i=7 7     dq=[7]         out 7
```

## Complexity
- Time: O(n), each index is pushed and popped once. Space: O(k).

## Pitfalls
- Store indices, not values, so you can tell when the front expires.

## Video Script
- Introduce the monotonic deque as a reusable tool; animate pushes and pops.

## Solution
```java file=slidingwindow/SlidingWindowMaximum.java
package slidingwindow;

import java.util.*;

/**
 * LC 239 Sliding Window Maximum.
 * Approach: monotonic decreasing deque of indices; front is the window max.
 * Time O(n), Space O(k).
 */
public class SlidingWindowMaximum {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] out = new int[nums.length - k + 1];
        Deque<Integer> dq = new ArrayDeque<>();
        for (int i = 0; i < nums.length; i++) {
            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) dq.pollLast();
            dq.offerLast(i);
            if (dq.peekFirst() <= i - k) dq.pollFirst();
            if (i >= k - 1) out[i - k + 1] = nums[dq.peekFirst()];
        }
        return out;
    }
}
```

## Tests
```java test=slidingwindow/SlidingWindowMaximumTest.java
package slidingwindow;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SlidingWindowMaximumTest {
    SlidingWindowMaximum s = new SlidingWindowMaximum();
    @Test void examples() {
        assertArrayEquals(new int[]{3, 3, 5, 5, 6, 7}, s.maxSlidingWindow(new int[]{1, 3, -1, -3, 5, 3, 6, 7}, 3));
        assertArrayEquals(new int[]{1}, s.maxSlidingWindow(new int[]{1}, 1));
        assertArrayEquals(new int[]{11}, s.maxSlidingWindow(new int[]{9, 11}, 2));
        assertArrayEquals(new int[]{7, 4}, s.maxSlidingWindow(new int[]{7, 2, 4}, 2));
    }
}
```
