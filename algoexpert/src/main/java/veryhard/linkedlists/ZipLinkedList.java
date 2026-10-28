package veryhard.linkedlists;

import common.LinkedListNode;

/**
 * Zip Linked List: reorder in place to first, last, second, second-to-last, ...
 * Split at middle, reverse second half, interleave.
 * Time: O(n) | Space: O(1).
 */
public class ZipLinkedList {
    public static LinkedListNode zipLinkedList(LinkedListNode head) {
        if (head == null || head.next == null) return head;
        LinkedListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) { slow = slow.next; fast = fast.next.next; }
        LinkedListNode second = slow.next, prev = null;
        slow.next = null;
        while (second != null) { LinkedListNode n = second.next; second.next = prev; prev = second; second = n; }
        LinkedListNode a = head, b = prev;
        while (b != null) {
            LinkedListNode an = a.next, bn = b.next;
            a.next = b; b.next = an;
            a = an; b = bn;
        }
        return head;
    }
}
