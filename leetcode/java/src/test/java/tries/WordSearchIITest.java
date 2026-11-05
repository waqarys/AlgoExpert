package tries;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class WordSearchIITest {
    static char[][] g(String... rows) {
        char[][] b = new char[rows.length][];
        for (int i = 0; i < rows.length; i++) b[i] = rows[i].toCharArray();
        return b;
    }
    @Test void examples() {
        var r = new WordSearchII().findWords(g("oaan", "etae", "ihkr", "iflv"), new String[]{"oath", "pea", "eat", "rain"});
        assertEquals(Set.of("oath", "eat"), new HashSet<>(r));
        assertEquals(List.of(), new WordSearchII().findWords(g("ab", "cd"), new String[]{"abcb"}));
        assertEquals(List.of("a"), new WordSearchII().findWords(g("a"), new String[]{"a", "a"}));
    }
}
