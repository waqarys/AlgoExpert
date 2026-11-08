package arrays;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ValidAnagramTest {
    ValidAnagram s = new ValidAnagram();
    @Test void examples() {
        assertTrue(s.isAnagram("anagram", "nagaram"));
        assertFalse(s.isAnagram("rat", "car"));
    }
    @Test void edges() {
        assertFalse(s.isAnagram("a", "ab"));
        assertTrue(s.isAnagram("", ""));
        assertFalse(s.isAnagram("aacc", "ccac"));
    }
}
