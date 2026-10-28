package veryhard.linkedlists;

import common.LinkedListNode;

/**
 * Rearrange Linked List: stable partition around k: nodes < k, then == k, then > k. Returns new head.
 * Time: O(n) | Space: O(1).
 */
public class RearrangeLinkedList {
    public static LinkedListNode rearrangeLinkedList(LinkedListNode head, int k) {
        LinkedListNode lo = new LinkedListNode(0), eq = new LinkedListNode(0), hi = new LinkedListNode(0);
        LinkedListNode l = lo, e = eq, h = hi;
        for (LinkedListNode c = head; c != null; c = c.next) {
            if (c.value < k) { l.next = c; l = c; }
            else if (c.value == k) { e.next = c; e = c; }
            else { h.next = c; h = c; }
        }
        h.next = null;
        e.next = hi.next;
        l.next = eq.next != null ? eq.next : hi.next;
        return lo.next;
    }
}
