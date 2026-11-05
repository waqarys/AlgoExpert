package dp2;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class EditDistanceTest {
    EditDistance s = new EditDistance();
    @Test void examples() {
        assertEquals(3, s.minDistance("horse", "ros"));
        assertEquals(5, s.minDistance("intention", "execution"));
        assertEquals(3, s.minDistance("", "abc"));
        assertEquals(0, s.minDistance("same", "same"));
    }
}
