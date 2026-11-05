package bits;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ReverseBitsTest {
    ReverseBits s = new ReverseBits();
    @Test void examples() {
        assertEquals(964176192, s.reverseBits(0b00000010100101000001111010011100));
        assertEquals(-1073741825, s.reverseBits(0b11111111111111111111111111111101));
        assertEquals(Integer.MIN_VALUE, s.reverseBits(1));
    }
}
