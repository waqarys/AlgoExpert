package medium.linkedlists;

/**
 * Linked List Construction: doubly linked list with head/tail supporting setHead, setTail, insertBefore,
 * insertAfter, insertAtPosition (1-based), removeNodesWithValue, remove and containsNodeWithValue.
 * Inserting a node already in the list moves it.
 * Time: O(1) for head/tail/insertBefore/After/remove, O(n) for position/value ops | Space: O(1).
 */
public class LinkedListConstruction {
    public static class Node {
        public int value;
        public Node prev, next;
        public Node(int value) { this.value = value; }
    }

    public static class DoublyLinkedList {
        public Node head, tail;

        public void setHead(Node n) {
            if (head == null) { head = tail = n; return; }
            insertBefore(head, n);
        }

        public void setTail(Node n) {
            if (tail == null) { setHead(n); return; }
            insertAfter(tail, n);
        }

        public void insertBefore(Node node, Node ins) {
            if (ins == head && ins == tail) return;
            remove(ins);
            ins.prev = node.prev;
            ins.next = node;
            if (node.prev == null) head = ins; else node.prev.next = ins;
            node.prev = ins;
        }

        public void insertAfter(Node node, Node ins) {
            if (ins == head && ins == tail) return;
            remove(ins);
            ins.prev = node;
            ins.next = node.next;
            if (node.next == null) tail = ins; else node.next.prev = ins;
            node.next = ins;
        }

        public void insertAtPosition(int pos, Node ins) {
            if (pos == 1) { setHead(ins); return; }
            Node cur = head;
            for (int p = 1; cur != null && p < pos; p++) cur = cur.next;
            if (cur != null) insertBefore(cur, ins); else setTail(ins);
        }

        public void removeNodesWithValue(int v) {
            Node cur = head;
            while (cur != null) { Node nx = cur.next; if (cur.value == v) remove(cur); cur = nx; }
        }

        public void remove(Node n) {
            if (n == head) head = head.next;
            if (n == tail) tail = tail.prev;
            if (n.prev != null) n.prev.next = n.next;
            if (n.next != null) n.next.prev = n.prev;
            n.prev = n.next = null;
        }

        public boolean containsNodeWithValue(int v) {
            for (Node c = head; c != null; c = c.next) if (c.value == v) return true;
            return false;
        }

        public java.util.List<Integer> values() {
            java.util.List<Integer> out = new java.util.ArrayList<>();
            for (Node c = head; c != null; c = c.next) out.add(c.value);
            return out;
        }
    }
}
