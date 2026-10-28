package hard.linkedlists;

import common.LinkedListNode;

/**
 * Reverse Linked List: reverse in place and return the new head.
 * Time: O(n) | Space: O(1).
 */
public class ReverseLinkedList {
    public static LinkedListNode reverseLinkedList(LinkedListNode head) {
        LinkedListNode prev = null;
        while (head != null) { LinkedListNode n = head.next; head.next = prev; prev = head; head = n; }
        return prev;
    }
}
