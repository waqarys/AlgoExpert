package linkedlist;

import common.ListNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ReorderListTest {
    int[] run(int... v) { ListNode h = ListNode.of(v); new ReorderList().reorderList(h); return ListNode.toArray(h); }
    @Test void examples() {
        assertArrayEquals(new int[]{1, 4, 2, 3}, run(1, 2, 3, 4));
        assertArrayEquals(new int[]{1, 5, 2, 4, 3}, run(1, 2, 3, 4, 5));
        assertArrayEquals(new int[]{1}, run(1));
        assertArrayEquals(new int[]{1, 2}, run(1, 2));
    }
}
