package bits;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CountingBitsTest {
    CountingBits s = new CountingBits();
    @Test void examples() {
        assertArrayEquals(new int[]{0, 1, 1}, s.countBits(2));
        assertArrayEquals(new int[]{0, 1, 1, 2, 1, 2}, s.countBits(5));
        assertArrayEquals(new int[]{0}, s.countBits(0));
    }
}
