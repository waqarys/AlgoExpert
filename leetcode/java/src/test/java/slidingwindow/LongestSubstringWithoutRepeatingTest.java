package slidingwindow;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LongestSubstringWithoutRepeatingTest {
    LongestSubstringWithoutRepeating s = new LongestSubstringWithoutRepeating();
    @Test void examples() {
        assertEquals(3, s.lengthOfLongestSubstring("abcabcbb"));
        assertEquals(1, s.lengthOfLongestSubstring("bbbbb"));
        assertEquals(3, s.lengthOfLongestSubstring("pwwkew"));
    }
    @Test void edges() {
        assertEquals(0, s.lengthOfLongestSubstring(""));
        assertEquals(2, s.lengthOfLongestSubstring("abba"));
        assertEquals(3, s.lengthOfLongestSubstring("a b"));
    }
}
