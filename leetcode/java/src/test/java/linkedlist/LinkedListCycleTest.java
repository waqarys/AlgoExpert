package linkedlist;

import common.ListNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LinkedListCycleTest {
    LinkedListCycle s = new LinkedListCycle();
    @Test void cycle() {
        ListNode h = ListNode.of(3, 2, 0, -4);
        h.next.next.next.next = h.next;
        assertTrue(s.hasCycle(h));
        ListNode one = ListNode.of(1);
        one.next = one;
        assertTrue(s.hasCycle(one));
    }
    @Test void noCycle() { assertFalse(s.hasCycle(ListNode.of(1, 2))); assertFalse(s.hasCycle(null)); }
}
