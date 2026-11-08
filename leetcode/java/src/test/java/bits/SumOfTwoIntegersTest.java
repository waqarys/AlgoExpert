package bits;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SumOfTwoIntegersTest {
    SumOfTwoIntegers s = new SumOfTwoIntegers();
    @Test void examples() {
        assertEquals(3, s.getSum(1, 2));
        assertEquals(5, s.getSum(2, 3));
        assertEquals(-1, s.getSum(-3, 2));
        assertEquals(-1000, s.getSum(-1000, 0));
        assertEquals(0, s.getSum(-7, 7));
    }
}
