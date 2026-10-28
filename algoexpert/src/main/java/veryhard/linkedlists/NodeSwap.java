package veryhard.linkedlists;

import common.LinkedListNode;

/**
 * Node Swap: swap every pair of adjacent nodes (not values); return the new head.
 * Time: O(n) | Space: O(1).
 */
public class NodeSwap {
    public static LinkedListNode nodeSwap(LinkedListNode head) {
        LinkedListNode dummy = new LinkedListNode(0);
        dummy.next = head;
        LinkedListNode p = dummy;
        while (p.next != null && p.next.next != null) {
            LinkedListNode a = p.next, b = a.next;
            a.next = b.next; b.next = a; p.next = b;
            p = a;
        }
        return dummy.next;
    }
}
