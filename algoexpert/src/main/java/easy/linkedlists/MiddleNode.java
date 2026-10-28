package easy.linkedlists;

import common.LinkedListNode;

/**
 * Middle Node: return the middle node (second middle for even lengths) via slow/fast pointers.
 * Time: O(n) | Space: O(1).
 */
public class MiddleNode {
    public static LinkedListNode middleNode(LinkedListNode head) {
        LinkedListNode slow = head, fast = head;
        while (fast != null && fast.next != null) { slow = slow.next; fast = fast.next.next; }
        return slow;
    }
}
