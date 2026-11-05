package dp2;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CoinChangeIITest {
    CoinChangeII s = new CoinChangeII();
    @Test void examples() {
        assertEquals(4, s.change(5, new int[]{1, 2, 5}));
        assertEquals(0, s.change(3, new int[]{2}));
        assertEquals(1, s.change(10, new int[]{10}));
        assertEquals(1, s.change(0, new int[]{7}));
    }
}
