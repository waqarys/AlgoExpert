package dp1;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class WordBreakTest {
    WordBreak s = new WordBreak();
    @Test void examples() {
        assertTrue(s.wordBreak("leetcode", List.of("leet", "code")));
        assertTrue(s.wordBreak("applepenapple", List.of("apple", "pen")));
        assertFalse(s.wordBreak("catsandog", List.of("cats", "dog", "sand", "and", "cat")));
    }
}
