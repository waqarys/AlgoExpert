package dp2;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class InterleavingStringTest {
    InterleavingString s = new InterleavingString();
    @Test void examples() {
        assertTrue(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"));
        assertFalse(s.isInterleave("aabcc", "dbbca", "aadbbbaccc"));
        assertTrue(s.isInterleave("", "", ""));
        assertFalse(s.isInterleave("a", "", "aa"));
    }
}
