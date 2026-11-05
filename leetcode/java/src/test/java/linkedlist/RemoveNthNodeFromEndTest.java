package linkedlist;

import common.ListNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class RemoveNthNodeFromEndTest {
    RemoveNthNodeFromEnd s = new RemoveNthNodeFromEnd();
    @Test void examples() {
        assertArrayEquals(new int[]{1, 2, 3, 5}, ListNode.toArray(s.removeNthFromEnd(ListNode.of(1, 2, 3, 4, 5), 2)));
        assertNull(s.removeNthFromEnd(ListNode.of(1), 1));
        assertArrayEquals(new int[]{1}, ListNode.toArray(s.removeNthFromEnd(ListNode.of(1, 2), 1)));
        assertArrayEquals(new int[]{2}, ListNode.toArray(s.removeNthFromEnd(ListNode.of(1, 2), 2)));
    }
}
