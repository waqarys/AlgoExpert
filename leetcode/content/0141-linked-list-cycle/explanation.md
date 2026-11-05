# 0141. Linked List Cycle

**Difficulty:** Easy | **Category:** Linked List | **LeetCode:** https://leetcode.com/problems/linked-list-cycle/

## Problem
- Return true if the linked list contains a cycle. Follow-up: O(1) memory.

## Intuition
- Floyd's tortoise and hare: slow moves 1 step, fast moves 2.
- In a cycle, fast gains one node per step on slow, so they must meet. Without a cycle, fast reaches null.

## Brute Force
- Store visited nodes in a HashSet: O(n) space.

## Optimal Approach
1. slow = fast = head.
2. While fast and fast.next: slow = slow.next; fast = fast.next.next; if slow == fast return true.
3. Return false.

## Worked Example
- 3 -> 2 -> 0 -> -4 -> (back to 2).
```text
step1 slow=2  fast=0
step2 slow=0  fast=2
step3 slow=-4 fast=-4  meet -> true
```

## Complexity
- Time: O(n). Space: O(1).

## Pitfalls
- Compare node references, not values.

## Video Script
- Running track analogy: a faster runner laps a slower one.

## Solution
```java file=linkedlist/LinkedListCycle.java
package linkedlist;

import common.ListNode;

/**
 * LC 141 Linked List Cycle.
 * Approach: Floyd's slow/fast pointers; they meet iff there is a cycle.
 * Time O(n), Space O(1).
 */
public class LinkedListCycle {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }
}
```

## Tests
```java test=linkedlist/LinkedListCycleTest.java
package linkedlist;

import common.ListNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LinkedListCycleTest {
    LinkedListCycle s = new LinkedListCycle();
    @Test void cycle() {
        ListNode h = ListNode.of(3, 2, 0, -4);
        h.next.next.next.next = h.next;
        assertTrue(s.hasCycle(h));
        ListNode one = ListNode.of(1);
        one.next = one;
        assertTrue(s.hasCycle(one));
    }
    @Test void noCycle() { assertFalse(s.hasCycle(ListNode.of(1, 2))); assertFalse(s.hasCycle(null)); }
}
```
