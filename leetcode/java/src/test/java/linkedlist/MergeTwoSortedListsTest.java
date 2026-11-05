package linkedlist;

import common.ListNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MergeTwoSortedListsTest {
    MergeTwoSortedLists s = new MergeTwoSortedLists();
    @Test void examples() {
        assertArrayEquals(new int[]{1, 1, 2, 3, 4, 4}, ListNode.toArray(s.mergeTwoLists(ListNode.of(1, 2, 4), ListNode.of(1, 3, 4))));
        assertNull(s.mergeTwoLists(null, null));
        assertArrayEquals(new int[]{0}, ListNode.toArray(s.mergeTwoLists(null, ListNode.of(0))));
    }
}
