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
