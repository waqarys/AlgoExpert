public class MergeLinkedLists {
    public static LinkedListNode mergeLinkedLists(LinkedListNode a, LinkedListNode b) {
        LinkedListNode dummy = new LinkedListNode(0), t = dummy;
        while (a != null && b != null) {
            if (a.value <= b.value) { t.next = a; a = a.next; } else { t.next = b; b = b.next; }
            t = t.next;
        }
        t.next = a != null ? a : b;
        return dummy.next;
    }
}
