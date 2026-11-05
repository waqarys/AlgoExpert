# 0206. Reverse Linked List

**Difficulty:** Easy | **Category:** Linked List | **LeetCode:** https://leetcode.com/problems/reverse-linked-list/

## Problem
- Reverse a singly linked list and return the new head.
- Example: 1->2->3->4->5 becomes 5->4->3->2->1.

## Intuition
- Walk the list once and flip each next pointer to point backwards.
- We need three references: prev (already reversed part), cur, and next (saved before we overwrite cur.next).

## Brute Force
- Copy values into an array and rebuild: O(n) extra space.

## Optimal Approach
1. prev = null, cur = head.
2. Loop: next = cur.next; cur.next = prev; prev = cur; cur = next.
3. Return prev.
4. Recursive version: reverse(head.next), then head.next.next = head; head.next = null.

## Worked Example
- 1->2->3.
```text
prev=null cur=1 : 1->null          prev=1 cur=2
prev=1    cur=2 : 2->1             prev=2 cur=3
prev=2    cur=3 : 3->2             prev=3 cur=null
return 3 (3->2->1)
```

## Complexity
- Iterative: O(n) time, O(1) space. Recursive: O(n) stack.

## Pitfalls
- Save next before overwriting cur.next, or you lose the rest of the list.

## Video Script
- The single most reused linked-list move; show it slowly with pointer arrows.

## Solution
```java file=linkedlist/ReverseLinkedList.java
package linkedlist;

import common.ListNode;

/**
 * LC 206 Reverse Linked List.
 * Approach: iterative pointer flip with prev/cur/next (recursive variant included).
 * Time O(n), Space O(1).
 */
public class ReverseLinkedList {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null, cur = head;
        while (cur != null) {
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }

    public ListNode reverseRecursive(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode newHead = reverseRecursive(head.next);
        head.next.next = head;
        head.next = null;
        return newHead;
    }
}
```

## Tests
```java test=linkedlist/ReverseLinkedListTest.java
package linkedlist;

import common.ListNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ReverseLinkedListTest {
    ReverseLinkedList s = new ReverseLinkedList();
    @Test void examples() {
        assertArrayEquals(new int[]{5, 4, 3, 2, 1}, ListNode.toArray(s.reverseList(ListNode.of(1, 2, 3, 4, 5))));
        assertArrayEquals(new int[]{2, 1}, ListNode.toArray(s.reverseRecursive(ListNode.of(1, 2))));
        assertNull(s.reverseList(null));
    }
}
```
