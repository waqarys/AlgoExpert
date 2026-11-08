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
