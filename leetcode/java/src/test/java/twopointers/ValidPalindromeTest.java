package twopointers;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ValidPalindromeTest {
    ValidPalindrome s = new ValidPalindrome();
    @Test void examples() {
        assertTrue(s.isPalindrome("A man, a plan, a canal: Panama"));
        assertFalse(s.isPalindrome("race a car"));
        assertTrue(s.isPalindrome(" "));
    }
    @Test void digits() { assertFalse(s.isPalindrome("0P")); assertTrue(s.isPalindrome("1a1")); }
}
