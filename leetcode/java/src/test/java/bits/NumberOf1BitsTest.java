package bits;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class NumberOf1BitsTest {
    NumberOf1Bits s = new NumberOf1Bits();
    @Test void examples() {
        assertEquals(3, s.hammingWeight(11));
        assertEquals(1, s.hammingWeight(128));
        assertEquals(31, s.hammingWeight(0xFFFFFFFD));
        assertEquals(0, s.hammingWeight(0));
    }
}
