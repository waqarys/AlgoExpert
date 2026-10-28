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
