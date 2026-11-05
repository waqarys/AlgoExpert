package math;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class PlusOneTest {
    PlusOne s = new PlusOne();
    @Test void examples() {
        assertArrayEquals(new int[]{1, 2, 4}, s.plusOne(new int[]{1, 2, 3}));
        assertArrayEquals(new int[]{1, 3, 0}, s.plusOne(new int[]{1, 2, 9}));
        assertArrayEquals(new int[]{1, 0, 0, 0}, s.plusOne(new int[]{9, 9, 9}));
        assertArrayEquals(new int[]{1}, s.plusOne(new int[]{0}));
    }
}
