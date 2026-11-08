package math;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MultiplyStringsTest {
    MultiplyStrings s = new MultiplyStrings();
    @Test void examples() {
        assertEquals("6", s.multiply("2", "3"));
        assertEquals("56088", s.multiply("123", "456"));
        assertEquals("5535", s.multiply("123", "45"));
        assertEquals("0", s.multiply("0", "999"));
        assertEquals("998001", s.multiply("999", "999"));
    }
}
