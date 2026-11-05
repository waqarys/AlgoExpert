package bits;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SingleNumberTest {
    SingleNumber s = new SingleNumber();
    @Test void examples() {
        assertEquals(1, s.singleNumber(new int[]{2, 2, 1}));
        assertEquals(4, s.singleNumber(new int[]{4, 1, 2, 1, 2}));
        assertEquals(-7, s.singleNumber(new int[]{-7}));
    }
}
