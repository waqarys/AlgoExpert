package veryhard.linkedlists;

import common.LinkedListNode;

/**
 * Linked List Palindrome: do the values read the same both ways? Reverse the second half, compare, restore.
 * Time: O(n) | Space: O(1).
 */
public class LinkedListPalindrome {
    public static boolean linkedListPalindrome(LinkedListNode head) {
        LinkedListNode slow = head, fast = head;
        while (fast != null && fast.next != null) { slow = slow.next; fast = fast.next.next; }
        LinkedListNode rev = reverse(slow), a = head, b = rev;
        boolean ok = true;
        while (b != null) { if (a.value != b.value) { ok = false; break; } a = a.next; b = b.next; }
        reverse(rev);
        return ok;
    }

    private static LinkedListNode reverse(LinkedListNode h) {
        LinkedListNode p = null;
        while (h != null) { LinkedListNode n = h.next; h.next = p; p = h; h = n; }
        return p;
    }
}
