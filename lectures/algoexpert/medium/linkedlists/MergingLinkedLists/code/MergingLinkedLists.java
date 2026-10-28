public class MergingLinkedLists {
    public static LinkedListNode mergingLinkedLists(LinkedListNode a, LinkedListNode b) {
        LinkedListNode p = a, q = b;
        while (p != q) { p = p == null ? b : p.next; q = q == null ? a : q.next; }
        return p;
    }
}
