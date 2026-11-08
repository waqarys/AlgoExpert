package advancedgraphs;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AlienDictionaryTest {
    AlienDictionary s = new AlienDictionary();
    @Test void examples() {
        assertEquals("wertf", s.alienOrder(new String[]{"wrt", "wrf", "er", "ett", "rftt"}));
        assertEquals("zx", s.alienOrder(new String[]{"z", "x"}));
        assertEquals("", s.alienOrder(new String[]{"z", "x", "z"}));
        assertEquals("", s.alienOrder(new String[]{"abc", "ab"}));
    }
}
