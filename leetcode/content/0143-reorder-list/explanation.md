# 0143. Reorder List

**Difficulty:** Medium | **Category:** Linked List | **LeetCode:** https://leetcode.com/problems/reorder-list/

## Problem
- Reorder L0->L1->...->Ln into L0->Ln->L1->Ln-1->... in place.
- Example: 1,2,3,4,5 -> 1,5,2,4,3.

## Intuition
- The result alternates between the front half and the reversed back half.
- So: find the middle, reverse the second half, then weave the two lists together.

## Brute Force
- Put nodes in an array and relink with two indices: O(n) extra space.

## Optimal Approach
1. Slow/fast pointers find the middle; cut after slow.
2. Reverse the second half (problem 206).
3. Merge alternately: a1, b1, a2, b2, ...

## Worked Example
- 1->2->3->4->5.
```text
middle at 3 -> first 1,2,3   second 4,5
reverse second -> 5,4
weave: 1,5,2,4,3
```

## Complexity
- Time: O(n). Space: O(1).

## Pitfalls
- Cut the list (slow.next = null) or you create a cycle.

## Video Script
- A "combo" problem: three building blocks - middle, reverse, merge - composed.

## Solution
```java file=linkedlist/ReorderList.java
package linkedlist;

import common.ListNode;

/**
 * LC 143 Reorder List.
 * Approach: find middle (slow/fast), reverse the second half, weave the halves.
 * Time O(n), Space O(1).
 */
public class ReorderList {
    public void reorderList(ListNode head) {
        if (head == null) return;
        ListNode slow = head, fast = head.next;
        while (fast != null && fast.next != null) { slow = slow.next; fast = fast.next.next; }
        ListNode second = slow.next, prev = null;
        slow.next = null;
        while (second != null) { ListNode nx = second.next; second.next = prev; prev = second; second = nx; }
        ListNode first = head;
        second = prev;
        while (second != null) {
            ListNode n1 = first.next, n2 = second.next;
            first.next = second;
            second.next = n1;
            first = n1;
            second = n2;
        }
    }
}
```

## Tests
```java test=linkedlist/ReorderListTest.java
package linkedlist;

import common.ListNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ReorderListTest {
    int[] run(int... v) { ListNode h = ListNode.of(v); new ReorderList().reorderList(h); return ListNode.toArray(h); }
    @Test void examples() {
        assertArrayEquals(new int[]{1, 4, 2, 3}, run(1, 2, 3, 4));
        assertArrayEquals(new int[]{1, 5, 2, 4, 3}, run(1, 2, 3, 4, 5));
        assertArrayEquals(new int[]{1}, run(1));
        assertArrayEquals(new int[]{1, 2}, run(1, 2));
    }
}
```
