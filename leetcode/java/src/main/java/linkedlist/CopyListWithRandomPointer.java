package linkedlist;

import java.util.*;

/**
 * LC 138 Copy List with Random Pointer.
 * Approach: interleave copies after each original, set randoms, then separate. O(1) extra space.
 * Time O(n), Space O(1) (excluding output).
 */
public class CopyListWithRandomPointer {
    public static class Node {
        public int val;
        public Node next, random;
        public Node(int val) { this.val = val; }
    }

    public Node copyRandomList(Node head) {
        for (Node n = head; n != null; n = n.next.next) {
            Node c = new Node(n.val);
            c.next = n.next;
            n.next = c;
        }
        for (Node n = head; n != null; n = n.next.next)
            if (n.random != null) n.next.random = n.random.next;
        Node dummy = new Node(0), tail = dummy;
        for (Node n = head; n != null; n = n.next) {
            tail.next = n.next;
            tail = tail.next;
            n.next = n.next.next;
        }
        return dummy.next;
    }

    /** HashMap version: easiest to explain. */
    public Node copyWithMap(Node head) {
        Map<Node, Node> map = new HashMap<>();
        for (Node n = head; n != null; n = n.next) map.put(n, new Node(n.val));
        for (Node n = head; n != null; n = n.next) {
            map.get(n).next = map.get(n.next);
            map.get(n).random = map.get(n.random);
        }
        return map.get(head);
    }
}
