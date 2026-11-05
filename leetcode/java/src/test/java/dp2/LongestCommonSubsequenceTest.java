package dp2;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LongestCommonSubsequenceTest {
    LongestCommonSubsequence s = new LongestCommonSubsequence();
    @Test void examples() {
        assertEquals(3, s.longestCommonSubsequence("abcde", "ace"));
        assertEquals(3, s.longestCommonSubsequence("abc", "abc"));
        assertEquals(0, s.longestCommonSubsequence("abc", "def"));
    }
}
