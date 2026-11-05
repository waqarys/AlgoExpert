package arrays;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ContainsDuplicateTest {
    ContainsDuplicate s = new ContainsDuplicate();
    @Test void examples() {
        assertTrue(s.containsDuplicate(new int[]{1, 2, 3, 1}));
        assertFalse(s.containsDuplicate(new int[]{1, 2, 3, 4}));
        assertTrue(s.containsDuplicate(new int[]{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}));
    }
    @Test void edges() {
        assertFalse(s.containsDuplicate(new int[]{}));
        assertFalse(s.containsDuplicate(new int[]{7}));
        assertTrue(s.containsDuplicateSort(new int[]{-1, 5, -1}));
    }
}
