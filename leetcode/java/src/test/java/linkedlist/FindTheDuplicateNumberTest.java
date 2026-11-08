package linkedlist;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class FindTheDuplicateNumberTest {
    FindTheDuplicateNumber s = new FindTheDuplicateNumber();
    @Test void examples() {
        assertEquals(2, s.findDuplicate(new int[]{1, 3, 4, 2, 2}));
        assertEquals(3, s.findDuplicate(new int[]{3, 1, 3, 4, 2}));
        assertEquals(3, s.findDuplicate(new int[]{3, 3, 3, 3, 3}));
        assertEquals(1, s.findDuplicate(new int[]{1, 1}));
    }
}
