package tries;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class WordDictionaryTest {
    @Test void example() {
        WordDictionary d = new WordDictionary();
        d.addWord("bad"); d.addWord("dad"); d.addWord("mad");
        assertFalse(d.search("pad"));
        assertTrue(d.search("bad"));
        assertTrue(d.search(".ad"));
        assertTrue(d.search("b.."));
        assertFalse(d.search("b..."));
        assertFalse(d.search("."));
    }
}
