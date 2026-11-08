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
