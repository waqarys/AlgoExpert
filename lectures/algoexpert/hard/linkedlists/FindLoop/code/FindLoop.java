public class FindLoop {
    public static LinkedListNode findLoop(LinkedListNode head) {
        LinkedListNode slow = head.next, fast = head.next.next;
        while (slow != fast) { slow = slow.next; fast = fast.next.next; }
        slow = head;
        while (slow != fast) { slow = slow.next; fast = fast.next; }
        return slow;
    }
}
