package medium.linkedlists;

import common.LinkedListNode;

/**
 * Sum Of Linked Lists: lists store digits least-significant first; return their sum in the same format.
 * Time: O(max(n, m)) | Space: O(max(n, m)).
 */
public class SumOfLinkedLists {
    public static LinkedListNode sumOfLinkedLists(LinkedListNode a, LinkedListNode b) {
        LinkedListNode dummy = new LinkedListNode(0), cur = dummy;
        int carry = 0;
        while (a != null || b != null || carry != 0) {
            int s = carry + (a == null ? 0 : a.value) + (b == null ? 0 : b.value);
            cur.next = new LinkedListNode(s % 10);
            cur = cur.next;
            carry = s / 10;
            if (a != null) a = a.next;
            if (b != null) b = b.next;
        }
        return dummy.next;
    }
}
