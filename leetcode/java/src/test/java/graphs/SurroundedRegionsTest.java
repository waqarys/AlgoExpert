package graphs;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SurroundedRegionsTest {
    static char[][] g(String... rows) {
        char[][] b = new char[rows.length][];
        for (int i = 0; i < rows.length; i++) b[i] = rows[i].toCharArray();
        return b;
    }
    @Test void examples() {
        char[][] b = g("XXXX", "XOOX", "XXOX", "XOXX");
        new SurroundedRegions().solve(b);
        assertArrayEquals(g("XXXX", "XXXX", "XXXX", "XOXX"), b);
        char[][] b2 = g("OO", "OO");
        new SurroundedRegions().solve(b2);
        assertArrayEquals(g("OO", "OO"), b2);
    }
}
