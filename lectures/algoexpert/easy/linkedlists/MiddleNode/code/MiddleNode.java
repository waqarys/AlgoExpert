public class MiddleNode {
    public static LinkedListNode middleNode(LinkedListNode head) {
        LinkedListNode slow = head, fast = head;
        while (fast != null && fast.next != null) { slow = slow.next; fast = fast.next.next; }
        return slow;
    }
}
