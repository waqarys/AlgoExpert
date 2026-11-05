package math;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class HappyNumberTest {
    HappyNumber s = new HappyNumber();
    @Test void examples() {
        assertTrue(s.isHappy(19));
        assertFalse(s.isHappy(2));
        assertTrue(s.isHappy(1));
        assertTrue(s.isHappy(7));
    }
}
