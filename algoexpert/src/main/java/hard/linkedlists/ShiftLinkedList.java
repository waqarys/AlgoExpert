package hard.linkedlists;

import common.LinkedListNode;

/**
 * Shift Linked List: rotate the list k positions forward (k > 0) or backward (k < 0); return the new head.
 * Time: O(n) | Space: O(1).
 */
public class ShiftLinkedList {
    public static LinkedListNode shiftLinkedList(LinkedListNode head, int k) {
        int len = 1;
        LinkedListNode tail = head;
        while (tail.next != null) { tail = tail.next; len++; }
        int shift = Math.floorMod(k, len);
        if (shift == 0) return head;
        LinkedListNode newTail = head;
        for (int i = 1; i < len - shift; i++) newTail = newTail.next;
        LinkedListNode newHead = newTail.next;
        newTail.next = null;
        tail.next = head;
        return newHead;
    }
}
