package dp2;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class DistinctSubsequencesTest {
    DistinctSubsequences s = new DistinctSubsequences();
    @Test void examples() {
        assertEquals(3, s.numDistinct("rabbbit", "rabbit"));
        assertEquals(5, s.numDistinct("babgbag", "bag"));
        assertEquals(0, s.numDistinct("abc", "abcd"));
        assertEquals(1, s.numDistinct("abc", ""));
    }
}
