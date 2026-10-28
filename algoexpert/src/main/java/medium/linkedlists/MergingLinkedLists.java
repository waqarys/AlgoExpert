package medium.linkedlists;

import common.LinkedListNode;

/**
 * Merging Linked Lists: two lists may converge into a shared tail; return the first shared node or null.
 * Two pointers that switch lists meet at the junction after at most n+m steps.
 * Time: O(n + m) | Space: O(1).
 */
public class MergingLinkedLists {
    public static LinkedListNode mergingLinkedLists(LinkedListNode a, LinkedListNode b) {
        LinkedListNode p = a, q = b;
        while (p != q) { p = p == null ? b : p.next; q = q == null ? a : q.next; }
        return p;
    }
}
