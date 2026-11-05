package dp1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LongestPalindromicSubstringTest {
    LongestPalindromicSubstring s = new LongestPalindromicSubstring();
    @Test void examples() {
        assertEquals("bab", s.longestPalindrome("babad"));
        assertEquals("bb", s.longestPalindrome("cbbd"));
        assertEquals("a", s.longestPalindrome("a"));
        assertEquals("racecar", s.longestPalindrome("xracecary"));
    }
}
