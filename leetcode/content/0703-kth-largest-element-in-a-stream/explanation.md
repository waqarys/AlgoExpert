# 0703. Kth Largest Element in a Stream

**Difficulty:** Easy | **Category:** Heap / Priority Queue | **LeetCode:** https://leetcode.com/problems/kth-largest-element-in-a-stream/

## Problem
- Design a class that, after each add(val), returns the k-th largest element seen so far.

## Intuition
- Keep only the k largest values in a min-heap of size k. Its top is the smallest of the top k, which is the k-th largest overall.

## Brute Force
- Keep a sorted list and insert each value: O(n) per add.

## Optimal Approach
1. Constructor: add every initial number through add().
2. add(val): offer val; if size > k, poll the minimum. Return peek().

## Worked Example
- k = 3, nums = [4,5,8,2].
```text
init heap keeps {4,5,8}
add 3  -> {3,4,5,8} -> drop 3 -> top 4
add 5  -> {4,5,5,8} -> drop 4 -> top 5
add 10 -> drop 5 -> {5,8,10} top 5
add 9  -> drop 5 -> {8,9,10} top 8
add 4  -> drop 4 -> top 8
```

## Complexity
- add: O(log k). Space: O(k).

## Pitfalls
- Min-heap, not max-heap: we discard the smallest of the candidates.

## Video Script
- Leaderboard analogy: only the top k scores matter, and the "entry bar" is the heap top.

## Solution
```java file=heap/KthLargest.java
package heap;

import java.util.*;

/**
 * LC 703 Kth Largest Element in a Stream.
 * Approach: min-heap holding the k largest values; top is the answer.
 * add O(log k), Space O(k).
 */
public class KthLargest {
    private final PriorityQueue<Integer> heap = new PriorityQueue<>();
    private final int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        for (int x : nums) add(x);
    }

    public int add(int val) {
        heap.offer(val);
        if (heap.size() > k) heap.poll();
        return heap.peek();
    }
}
```

## Tests
```java test=heap/KthLargestTest.java
package heap;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class KthLargestTest {
    @Test void example() {
        KthLargest k = new KthLargest(3, new int[]{4, 5, 8, 2});
        assertEquals(4, k.add(3));
        assertEquals(5, k.add(5));
        assertEquals(5, k.add(10));
        assertEquals(8, k.add(9));
        assertEquals(8, k.add(4));
    }
    @Test void startsEmpty() {
        KthLargest k = new KthLargest(1, new int[]{});
        assertEquals(-3, k.add(-3));
        assertEquals(-2, k.add(-2));
    }
}
```
