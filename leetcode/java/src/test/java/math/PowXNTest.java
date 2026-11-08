package math;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class PowXNTest {
    PowXN s = new PowXN();
    @Test void examples() {
        assertEquals(1024.0, s.myPow(2.0, 10), 1e-9);
        assertEquals(9.261, s.myPow(2.1, 3), 1e-9);
        assertEquals(0.25, s.myPow(2.0, -2), 1e-9);
        assertEquals(1.0, s.myPow(1.0, Integer.MIN_VALUE), 1e-9);
        assertEquals(1.0, s.myPow(5.0, 0), 1e-9);
    }
}
