package graphs;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class WordLadderTest {
    WordLadder s = new WordLadder();
    @Test void examples() {
        assertEquals(5, s.ladderLength("hit", "cog", List.of("hot", "dot", "dog", "lot", "log", "cog")));
        assertEquals(0, s.ladderLength("hit", "cog", List.of("hot", "dot", "dog", "lot", "log")));
        assertEquals(2, s.ladderLength("a", "c", List.of("a", "b", "c")));
    }
}
