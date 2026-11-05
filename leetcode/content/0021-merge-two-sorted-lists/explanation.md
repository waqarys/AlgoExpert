# 0021. Merge Two Sorted Lists

**Difficulty:** Easy | **Category:** Linked List | **LeetCode:** https://leetcode.com/problems/merge-two-sorted-lists/

## Problem
- Merge two sorted linked lists into one sorted list by splicing their nodes.
- Example: 1->2->4 and 1->3->4 -> 1->1->2->3->4->4.

## Intuition
- Like the merge step of merge sort: repeatedly take the smaller head.
- A dummy node removes the special case for the first node.

## Brute Force
- Collect all values, sort, and rebuild: O((m+n) log(m+n)).

## Optimal Approach
1. dummy -> tail.
2. While both non-null: attach the smaller node, advance that list and tail.
3. Attach the remaining list.

## Worked Example
- a = 1->2->4, b = 1->3->4.
```text
1 vs 1 -> take a1   | 2 vs 1 -> take b1
2 vs 3 -> take a2   | 4 vs 3 -> take b3
4 vs 4 -> take a4   | a empty -> append b4
result 1,1,2,3,4,4
```

## Complexity
- Time: O(m+n). Space: O(1).

## Pitfalls
- Forgetting to append the leftover list.

## Video Script
- Introduce the dummy-node pattern; it appears in most list-building problems.

## Solution
```java file=linkedlist/MergeTwoSortedLists.java
package linkedlist;

import common.ListNode;

/**
 * LC 21 Merge Two Sorted Lists.
 * Approach: dummy head + tail pointer; take the smaller head each step.
 * Time O(m+n), Space O(1).
 */
public class MergeTwoSortedLists {
    public ListNode mergeTwoLists(ListNode a, ListNode b) {
        ListNode dummy = new ListNode(0), tail = dummy;
        while (a != null && b != null) {
            if (a.val <= b.val) { tail.next = a; a = a.next; }
            else { tail.next = b; b = b.next; }
            tail = tail.next;
        }
        tail.next = a != null ? a : b;
        return dummy.next;
    }
}
```

## Tests
```java test=linkedlist/MergeTwoSortedListsTest.java
package linkedlist;

import common.ListNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MergeTwoSortedListsTest {
    MergeTwoSortedLists s = new MergeTwoSortedLists();
    @Test void examples() {
        assertArrayEquals(new int[]{1, 1, 2, 3, 4, 4}, ListNode.toArray(s.mergeTwoLists(ListNode.of(1, 2, 4), ListNode.of(1, 3, 4))));
        assertNull(s.mergeTwoLists(null, null));
        assertArrayEquals(new int[]{0}, ListNode.toArray(s.mergeTwoLists(null, ListNode.of(0))));
    }
}
```
