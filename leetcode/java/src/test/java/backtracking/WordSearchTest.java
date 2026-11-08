package backtracking;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class WordSearchTest {
    static char[][] g() { return new char[][]{"ABCE".toCharArray(), "SFCS".toCharArray(), "ADEE".toCharArray()}; }
    WordSearch s = new WordSearch();
    @Test void examples() {
        assertTrue(s.exist(g(), "ABCCED"));
        assertTrue(s.exist(g(), "SEE"));
        assertFalse(s.exist(g(), "ABCB"));
        assertTrue(s.exist(new char[][]{{'a'}}, "a"));
    }
}
