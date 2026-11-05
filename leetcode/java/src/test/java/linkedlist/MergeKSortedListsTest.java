package linkedlist;

import common.ListNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MergeKSortedListsTest {
    MergeKSortedLists s = new MergeKSortedLists();
    @Test void examples() {
        ListNode r = s.mergeKLists(new ListNode[]{ListNode.of(1, 4, 5), ListNode.of(1, 3, 4), ListNode.of(2, 6)});
        assertArrayEquals(new int[]{1, 1, 2, 3, 4, 4, 5, 6}, ListNode.toArray(r));
        assertNull(s.mergeKLists(new ListNode[]{}));
        assertNull(s.mergeKLists(new ListNode[]{null}));
    }
}
