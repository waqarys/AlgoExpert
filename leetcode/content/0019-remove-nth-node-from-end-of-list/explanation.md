# 0019. Remove Nth Node From End of List

**Difficulty:** Medium | **Category:** Linked List | **LeetCode:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/

## Problem
- Remove the n-th node from the end of the list and return the head, ideally in one pass.
- Example: 1,2,3,4,5 with n = 2 -> 1,2,3,5.

## Intuition
- Keep two pointers n nodes apart. When the front pointer falls off the end, the back pointer sits just before the node to delete.
- Starting from a dummy node handles deleting the head.

## Brute Force
- Count the length L, then walk L - n steps: two passes.

## Optimal Approach
1. dummy.next = head; fast = slow = dummy.
2. Move fast n+1 steps.
3. Move both until fast is null; slow.next is the target.
4. slow.next = slow.next.next.

## Worked Example
- 1,2,3,4,5, n = 2.
```text
fast moves 3 steps: dummy -> 1 -> 2 -> 3
move both: (slow=1,fast=4) (2,5) (3,null)
slow=3 -> remove 4 -> 1,2,3,5
```

## Complexity
- Time: O(L). Space: O(1).

## Pitfalls
- Removing the head (n == length) is why the dummy node exists.

## Video Script
- "Fixed-gap two pointers" - a ruler sliding along the list.

## Solution
```java file=linkedlist/RemoveNthNodeFromEnd.java
package linkedlist;

import common.ListNode;

/**
 * LC 19 Remove Nth Node From End of List.
 * Approach: dummy + two pointers spaced n+1 apart; one pass.
 * Time O(L), Space O(1).
 */
public class RemoveNthNodeFromEnd {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head), fast = dummy, slow = dummy;
        for (int i = 0; i <= n; i++) fast = fast.next;
        while (fast != null) { fast = fast.next; slow = slow.next; }
        slow.next = slow.next.next;
        return dummy.next;
    }
}
```

## Tests
```java test=linkedlist/RemoveNthNodeFromEndTest.java
package linkedlist;

import common.ListNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class RemoveNthNodeFromEndTest {
    RemoveNthNodeFromEnd s = new RemoveNthNodeFromEnd();
    @Test void examples() {
        assertArrayEquals(new int[]{1, 2, 3, 5}, ListNode.toArray(s.removeNthFromEnd(ListNode.of(1, 2, 3, 4, 5), 2)));
        assertNull(s.removeNthFromEnd(ListNode.of(1), 1));
        assertArrayEquals(new int[]{1}, ListNode.toArray(s.removeNthFromEnd(ListNode.of(1, 2), 1)));
        assertArrayEquals(new int[]{2}, ListNode.toArray(s.removeNthFromEnd(ListNode.of(1, 2), 2)));
    }
}
```
