public class ReverseLinkedList {
    public static LinkedListNode reverseLinkedList(LinkedListNode head) {
        LinkedListNode prev = null;
        while (head != null) { LinkedListNode n = head.next; head.next = prev; prev = head; head = n; }
        return prev;
    }
}
