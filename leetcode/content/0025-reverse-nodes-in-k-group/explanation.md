# 0025. Reverse Nodes in k-Group

**Difficulty:** Hard | **Category:** Linked List | **LeetCode:** https://leetcode.com/problems/reverse-nodes-in-k-group/

## Problem
- Reverse the list k nodes at a time; a final group shorter than k stays as is. O(1) extra memory.
- Example: 1..5, k = 2 -> 2,1,4,3,5; k = 3 -> 3,2,1,4,5.

## Intuition
- Process groups one by one: check that k nodes exist, reverse exactly those k, then reconnect with the previous group's tail and the next group's head.
- groupPrev is the node before the current group; after reversal, the group's original first node becomes the new groupPrev.

## Brute Force
- Copy values into an array, reverse chunks, rebuild: O(n) extra space.

## Optimal Approach
1. dummy -> head; groupPrev = dummy.
2. kth = walk k steps from groupPrev; if null, stop.
3. groupNext = kth.next. Reverse nodes from groupPrev.next up to kth, with prev starting at groupNext.
4. first = groupPrev.next; groupPrev.next = kth; groupPrev = first.

## Worked Example
- 1,2,3,4,5 with k = 2.
```text
group [1,2] -> 2,1   list: 2,1,3,4,5   groupPrev=1
group [3,4] -> 4,3   list: 2,1,4,3,5   groupPrev=3
group [5] has < 2 nodes -> stop
```

## Complexity
- Time: O(n). Space: O(1).

## Pitfalls
- Initialising prev = groupNext makes the reversed tail point to the next group automatically.

## Video Script
- Composition again: problem 206 applied per window, with careful reconnection drawn on screen.

## Solution
```java file=linkedlist/ReverseNodesInKGroup.java
package linkedlist;

import common.ListNode;

/**
 * LC 25 Reverse Nodes in k-Group.
 * Approach: per group, verify k nodes, reverse in place with prev = groupNext, reconnect.
 * Time O(n), Space O(1).
 */
public class ReverseNodesInKGroup {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(0, head), groupPrev = dummy;
        while (true) {
            ListNode kth = groupPrev;
            for (int i = 0; i < k && kth != null; i++) kth = kth.next;
            if (kth == null) break;
            ListNode groupNext = kth.next, prev = groupNext, cur = groupPrev.next;
            while (cur != groupNext) {
                ListNode nx = cur.next;
                cur.next = prev;
                prev = cur;
                cur = nx;
            }
            ListNode first = groupPrev.next;
            groupPrev.next = kth;
            groupPrev = first;
        }
        return dummy.next;
    }
}
```

## Tests
```java test=linkedlist/ReverseNodesInKGroupTest.java
package linkedlist;

import common.ListNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ReverseNodesInKGroupTest {
    int[] run(int k, int... v) { return ListNode.toArray(new ReverseNodesInKGroup().reverseKGroup(ListNode.of(v), k)); }
    @Test void examples() {
        assertArrayEquals(new int[]{2, 1, 4, 3, 5}, run(2, 1, 2, 3, 4, 5));
        assertArrayEquals(new int[]{3, 2, 1, 4, 5}, run(3, 1, 2, 3, 4, 5));
        assertArrayEquals(new int[]{1, 2, 3}, run(1, 1, 2, 3));
        assertArrayEquals(new int[]{4, 3, 2, 1}, run(4, 1, 2, 3, 4));
    }
}
```
