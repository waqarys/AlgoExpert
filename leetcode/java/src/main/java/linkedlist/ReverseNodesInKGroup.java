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
