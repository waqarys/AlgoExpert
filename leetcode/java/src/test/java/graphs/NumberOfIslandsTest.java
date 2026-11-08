package graphs;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class NumberOfIslandsTest {
    static char[][] g(String... rows) {
        char[][] b = new char[rows.length][];
        for (int i = 0; i < rows.length; i++) b[i] = rows[i].toCharArray();
        return b;
    }
    NumberOfIslands s = new NumberOfIslands();
    @Test void examples() {
        assertEquals(1, s.numIslands(g("11110", "11010", "11000", "00000")));
        assertEquals(3, s.numIslands(g("11000", "11000", "00100", "00011")));
        assertEquals(0, s.numIslands(g("0")));
        assertEquals(2, s.numIslands(g("10", "01")));
    }
}
