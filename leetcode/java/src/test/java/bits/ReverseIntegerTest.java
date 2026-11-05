package bits;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ReverseIntegerTest {
    ReverseInteger s = new ReverseInteger();
    @Test void examples() {
        assertEquals(321, s.reverse(123));
        assertEquals(-321, s.reverse(-123));
        assertEquals(21, s.reverse(120));
        assertEquals(0, s.reverse(1534236469));
        assertEquals(0, s.reverse(Integer.MIN_VALUE));
        assertEquals(0, s.reverse(0));
    }
}
