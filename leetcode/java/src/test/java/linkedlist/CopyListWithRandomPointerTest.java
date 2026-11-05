package linkedlist;

import linkedlist.CopyListWithRandomPointer.Node;
import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class CopyListWithRandomPointerTest {
    static Node build(int[][] spec) {
        Node[] ns = new Node[spec.length];
        for (int i = 0; i < spec.length; i++) ns[i] = new Node(spec[i][0]);
        for (int i = 0; i < spec.length; i++) {
            if (i + 1 < spec.length) ns[i].next = ns[i + 1];
            if (spec[i][1] >= 0) ns[i].random = ns[spec[i][1]];
        }
        return spec.length == 0 ? null : ns[0];
    }
    static List<String> dump(Node h) {
        List<Node> order = new ArrayList<>();
        for (Node n = h; n != null; n = n.next) order.add(n);
        List<String> out = new ArrayList<>();
        for (Node n : order) out.add(n.val + ":" + (n.random == null ? -1 : order.indexOf(n.random)));
        return out;
    }
    int[][] spec = {{7, -1}, {13, 0}, {11, 4}, {10, 2}, {1, 0}};
    @Test void interleave() {
        Node h = build(spec);
        List<String> before = dump(h);
        Node c = new CopyListWithRandomPointer().copyRandomList(h);
        assertEquals(before, dump(c));
        assertEquals(before, dump(h)); // original restored
        assertNotSame(h, c);
        assertNotSame(h.next.random, c.next.random);
    }
    @Test void map() {
        Node h = build(spec);
        assertEquals(dump(h), dump(new CopyListWithRandomPointer().copyWithMap(h)));
        assertNull(new CopyListWithRandomPointer().copyRandomList(null));
    }
}
