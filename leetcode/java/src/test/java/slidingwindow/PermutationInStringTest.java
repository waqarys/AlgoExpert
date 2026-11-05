package slidingwindow;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class PermutationInStringTest {
    PermutationInString s = new PermutationInString();
    @Test void examples() {
        assertTrue(s.checkInclusion("ab", "eidbaooo"));
        assertFalse(s.checkInclusion("ab", "eidboaoo"));
    }
    @Test void edges() {
        assertFalse(s.checkInclusion("abc", "ab"));
        assertTrue(s.checkInclusion("adc", "dcda"));
        assertTrue(s.checkInclusion("a", "a"));
    }
}
