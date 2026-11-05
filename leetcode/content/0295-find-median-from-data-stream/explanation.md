# 0295. Find Median from Data Stream

**Difficulty:** Hard | **Category:** Heap / Priority Queue | **LeetCode:** https://leetcode.com/problems/find-median-from-data-stream/

## Problem
- Support addNum(x) and findMedian() over a growing stream.

## Intuition
- Split the numbers into a lower half (max-heap) and an upper half (min-heap).
- Keep sizes balanced (lower may hold one extra). The median is lower's top, or the average of both tops.

## Brute Force
- Keep a sorted list with insertion: O(n) per add.

## Optimal Approach
1. addNum: push to lower; move lower's top to upper (keeps the order invariant).
2. If upper is bigger than lower, move upper's top back to lower.
3. findMedian: sizes equal -> average of tops; else lower.peek().

## Worked Example
```text
add 1: lower {1}           median 1
add 2: lower {1} upper {2} median 1.5
add 3: lower {2,1} upper {3}  median 2
```

## Complexity
- addNum O(log n), findMedian O(1). Space O(n).

## Pitfalls
- Average as double; sum of two ints can overflow, so cast before adding.

## Video Script
- Draw two piles facing each other; the median sits where they meet.

## Solution
```java file=heap/MedianFinder.java
package heap;

import java.util.*;

/**
 * LC 295 Find Median from Data Stream.
 * Approach: max-heap for the lower half, min-heap for the upper half, kept balanced.
 * add O(log n), median O(1).
 */
public class MedianFinder {
    private final PriorityQueue<Integer> lower = new PriorityQueue<>(Collections.reverseOrder());
    private final PriorityQueue<Integer> upper = new PriorityQueue<>();

    public void addNum(int num) {
        lower.offer(num);
        upper.offer(lower.poll());
        if (upper.size() > lower.size()) lower.offer(upper.poll());
    }

    public double findMedian() {
        if (lower.size() > upper.size()) return lower.peek();
        return ((double) lower.peek() + upper.peek()) / 2.0;
    }
}
```

## Tests
```java test=heap/MedianFinderTest.java
package heap;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MedianFinderTest {
    @Test void example() {
        MedianFinder m = new MedianFinder();
        m.addNum(1); m.addNum(2);
        assertEquals(1.5, m.findMedian());
        m.addNum(3);
        assertEquals(2.0, m.findMedian());
    }
    @Test void largeAndNegative() {
        MedianFinder m = new MedianFinder();
        m.addNum(Integer.MAX_VALUE); m.addNum(Integer.MAX_VALUE);
        assertEquals((double) Integer.MAX_VALUE, m.findMedian());
        m.addNum(-5);
        assertEquals((double) Integer.MAX_VALUE, m.findMedian());
    }
}
```
