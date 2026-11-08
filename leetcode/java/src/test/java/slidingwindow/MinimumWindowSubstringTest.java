package slidingwindow;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MinimumWindowSubstringTest {
    MinimumWindowSubstring s = new MinimumWindowSubstring();
    @Test void examples() {
        assertEquals("BANC", s.minWindow("ADOBECODEBANC", "ABC"));
        assertEquals("a", s.minWindow("a", "a"));
        assertEquals("", s.minWindow("a", "aa"));
    }
    @Test void duplicates() { assertEquals("baa", s.minWindow("bbaa", "aba")); }
}
