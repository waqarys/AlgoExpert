package hard.linkedlists;

import common.LinkedListNode;

/**
 * Find Loop: the list contains a cycle; return the node where the loop begins (Floyd's algorithm).
 * Time: O(n) | Space: O(1).
 */
public class FindLoop {
    public static LinkedListNode findLoop(LinkedListNode head) {
        LinkedListNode slow = head.next, fast = head.next.next;
        while (slow != fast) { slow = slow.next; fast = fast.next.next; }
        slow = head;
        while (slow != fast) { slow = slow.next; fast = fast.next; }
        return slow;
    }
}
