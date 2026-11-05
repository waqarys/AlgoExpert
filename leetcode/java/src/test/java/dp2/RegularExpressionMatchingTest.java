package dp2;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class RegularExpressionMatchingTest {
    RegularExpressionMatching s = new RegularExpressionMatching();
    @Test void examples() {
        assertFalse(s.isMatch("aa", "a"));
        assertTrue(s.isMatch("aa", "a*"));
        assertTrue(s.isMatch("ab", ".*"));
        assertTrue(s.isMatch("aab", "c*a*b"));
        assertFalse(s.isMatch("mississippi", "mis*is*p*."));
        assertTrue(s.isMatch("", "a*b*"));
    }
}
