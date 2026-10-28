package easy.linkedlists;

import common.LinkedListNode;

/**
 * Remove Duplicates From Linked List: list is sorted; remove nodes with repeated values in place.
 * Time: O(n) | Space: O(1).
 */
public class RemoveDuplicatesFromLinkedList {
    public static LinkedListNode removeDuplicatesFromLinkedList(LinkedListNode head) {
        LinkedListNode cur = head;
        while (cur != null) {
            LinkedListNode next = cur.next;
            while (next != null && next.value == cur.value) next = next.next;
            cur.next = next;
            cur = next;
        }
        return head;
    }
}
