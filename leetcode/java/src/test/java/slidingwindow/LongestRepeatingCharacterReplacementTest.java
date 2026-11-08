package slidingwindow;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LongestRepeatingCharacterReplacementTest {
    LongestRepeatingCharacterReplacement s = new LongestRepeatingCharacterReplacement();
    @Test void examples() {
        assertEquals(4, s.characterReplacement("ABAB", 2));
        assertEquals(4, s.characterReplacement("AABABBA", 1));
    }
    @Test void edges() {
        assertEquals(1, s.characterReplacement("A", 0));
        assertEquals(2, s.characterReplacement("ABCD", 1));
        assertEquals(5, s.characterReplacement("AAAAA", 0));
    }
}
