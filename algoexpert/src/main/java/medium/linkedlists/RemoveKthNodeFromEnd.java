package medium.linkedlists;

import common.LinkedListNode;

/**
 * Remove Kth Node From End: remove in place (list length >= 2, k valid). If the head is removed, the head
 * node takes its successor's value so the reference stays valid.
 * Time: O(n) | Space: O(1).
 */
public class RemoveKthNodeFromEnd {
    public static void removeKthNodeFromEnd(LinkedListNode head, int k) {
        LinkedListNode fast = head, slow = head;
        for (int i = 0; i < k; i++) fast = fast.next;
        if (fast == null) { head.value = head.next.value; head.next = head.next.next; return; }
        while (fast.next != null) { fast = fast.next; slow = slow.next; }
        slow.next = slow.next.next;
    }
}
