package dp1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class PalindromicSubstringsTest {
    PalindromicSubstrings s = new PalindromicSubstrings();
    @Test void examples() {
        assertEquals(3, s.countSubstrings("abc"));
        assertEquals(6, s.countSubstrings("aaa"));
        assertEquals(1, s.countSubstrings("x"));
    }
}
