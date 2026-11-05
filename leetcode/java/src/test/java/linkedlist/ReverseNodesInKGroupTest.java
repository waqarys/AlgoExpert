package linkedlist;

import common.ListNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ReverseNodesInKGroupTest {
    int[] run(int k, int... v) { return ListNode.toArray(new ReverseNodesInKGroup().reverseKGroup(ListNode.of(v), k)); }
    @Test void examples() {
        assertArrayEquals(new int[]{2, 1, 4, 3, 5}, run(2, 1, 2, 3, 4, 5));
        assertArrayEquals(new int[]{3, 2, 1, 4, 5}, run(3, 1, 2, 3, 4, 5));
        assertArrayEquals(new int[]{1, 2, 3}, run(1, 1, 2, 3));
        assertArrayEquals(new int[]{4, 3, 2, 1}, run(4, 1, 2, 3, 4));
    }
}
