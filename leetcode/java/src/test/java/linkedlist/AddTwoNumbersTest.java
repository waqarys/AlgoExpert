package linkedlist;

import common.ListNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AddTwoNumbersTest {
    AddTwoNumbers s = new AddTwoNumbers();
    @Test void examples() {
        assertArrayEquals(new int[]{7, 0, 8}, ListNode.toArray(s.addTwoNumbers(ListNode.of(2, 4, 3), ListNode.of(5, 6, 4))));
        assertArrayEquals(new int[]{0}, ListNode.toArray(s.addTwoNumbers(ListNode.of(0), ListNode.of(0))));
        assertArrayEquals(new int[]{8, 9, 9, 9, 0, 0, 0, 1},
                ListNode.toArray(s.addTwoNumbers(ListNode.of(9, 9, 9, 9, 9, 9, 9), ListNode.of(9, 9, 9, 9))));
    }
}
