package linkedlist;

import common.ListNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ReverseLinkedListTest {
    ReverseLinkedList s = new ReverseLinkedList();
    @Test void examples() {
        assertArrayEquals(new int[]{5, 4, 3, 2, 1}, ListNode.toArray(s.reverseList(ListNode.of(1, 2, 3, 4, 5))));
        assertArrayEquals(new int[]{2, 1}, ListNode.toArray(s.reverseRecursive(ListNode.of(1, 2))));
        assertNull(s.reverseList(null));
    }
}
