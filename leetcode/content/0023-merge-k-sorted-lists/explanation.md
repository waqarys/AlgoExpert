# 0023. Merge k Sorted Lists

**Difficulty:** Hard | **Category:** Linked List | **LeetCode:** https://leetcode.com/problems/merge-k-sorted-lists/

## Problem
- Merge k sorted linked lists into one sorted list.
- Example: [1,4,5],[1,3,4],[2,6] -> 1,1,2,3,4,4,5,6.

## Intuition
- At each step the next node is the smallest among k current heads; a min-heap gives that in O(log k).
- Alternative: divide and conquer, merging lists in pairs (like merge sort), also O(N log k).

## Brute Force
- Merge lists one by one into an accumulator: O(N * k).

## Optimal Approach
1. Push every non-null head into a min-heap keyed by val.
2. Pop the smallest, append it, push its next if non-null.
3. Repeat until the heap is empty.

## Worked Example
```text
heap {1a,1b,2c}   pop 1a push 4a
heap {1b,2c,4a}   pop 1b push 3b
heap {2c,3b,4a}   pop 2c push 6c
heap {3b,4a,6c}   pop 3b push 4b
... output 1,1,2,3,4,4,5,6
```

## Complexity
- Time: O(N log k), N = total nodes. Space: O(k).

## Pitfalls
- Skip null lists when seeding the heap.
- Use Integer.compare in the comparator to avoid subtraction overflow.

## Video Script
- Show the k-way merge as "k queues at a ticket counter, always serve the smallest".

## Solution
```java file=linkedlist/MergeKSortedLists.java
package linkedlist;

import common.ListNode;
import java.util.*;

/**
 * LC 23 Merge k Sorted Lists.
 * Approach: min-heap of current heads; pop smallest, push its successor.
 * Time O(N log k), Space O(k).
 */
public class MergeKSortedLists {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> Integer.compare(a.val, b.val));
        for (ListNode l : lists) if (l != null) pq.add(l);
        ListNode dummy = new ListNode(0), tail = dummy;
        while (!pq.isEmpty()) {
            ListNode n = pq.poll();
            tail.next = n;
            tail = n;
            if (n.next != null) pq.add(n.next);
        }
        return dummy.next;
    }
}
```

## Tests
```java test=linkedlist/MergeKSortedListsTest.java
package linkedlist;

import common.ListNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MergeKSortedListsTest {
    MergeKSortedLists s = new MergeKSortedLists();
    @Test void examples() {
        ListNode r = s.mergeKLists(new ListNode[]{ListNode.of(1, 4, 5), ListNode.of(1, 3, 4), ListNode.of(2, 6)});
        assertArrayEquals(new int[]{1, 1, 2, 3, 4, 4, 5, 6}, ListNode.toArray(r));
        assertNull(s.mergeKLists(new ListNode[]{}));
        assertNull(s.mergeKLists(new ListNode[]{null}));
    }
}
```
