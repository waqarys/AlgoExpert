package linkedlist;

import common.ListNode;

/**
 * LC 206 Reverse Linked List.
 * Approach: iterative pointer flip with prev/cur/next (recursive variant included).
 * Time O(n), Space O(1).
 */
public class ReverseLinkedList {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null, cur = head;
        while (cur != null) {
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }

    public ListNode reverseRecursive(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode newHead = reverseRecursive(head.next);
        head.next.next = head;
        head.next = null;
        return newHead;
    }
}
