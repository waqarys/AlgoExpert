package common;

import java.util.ArrayList;
import java.util.List;

/** Shared singly linked list node used by linked-list problems. */
public class LinkedListNode {
    public int value;
    public LinkedListNode next;

    public LinkedListNode(int value) { this.value = value; }

    public static LinkedListNode of(int... values) {
        LinkedListNode dummy = new LinkedListNode(0), cur = dummy;
        for (int v : values) { cur.next = new LinkedListNode(v); cur = cur.next; }
        return dummy.next;
    }

    public static List<Integer> toList(LinkedListNode head) {
        List<Integer> out = new ArrayList<>();
        for (LinkedListNode c = head; c != null; c = c.next) out.add(c.value);
        return out;
    }
}
