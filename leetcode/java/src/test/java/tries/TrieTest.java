package tries;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TrieTest {
    @Test void example() {
        Trie t = new Trie();
        t.insert("apple");
        assertTrue(t.search("apple"));
        assertFalse(t.search("app"));
        assertTrue(t.startsWith("app"));
        t.insert("app");
        assertTrue(t.search("app"));
        assertFalse(t.startsWith("b"));
    }
}
