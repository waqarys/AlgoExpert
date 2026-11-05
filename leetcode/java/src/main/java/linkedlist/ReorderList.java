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
