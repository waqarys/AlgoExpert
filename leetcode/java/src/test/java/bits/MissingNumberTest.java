package bits;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MissingNumberTest {
    MissingNumber s = new MissingNumber();
    @Test void examples() {
        assertEquals(2, s.missingNumber(new int[]{3, 0, 1}));
        assertEquals(2, s.missingNumber(new int[]{0, 1}));
        assertEquals(8, s.missingNumber(new int[]{9, 6, 4, 2, 3, 5, 7, 0, 1}));
        assertEquals(0, s.missingNumber(new int[]{1}));
    }
}
