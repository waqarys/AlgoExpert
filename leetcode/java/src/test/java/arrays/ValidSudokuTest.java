package arrays;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ValidSudokuTest {
    static char[][] b(String... rows) {
        char[][] g = new char[9][];
        for (int i = 0; i < 9; i++) g[i] = rows[i].toCharArray();
        return g;
    }
    static final String[] VALID = {"53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1",
            "7...2...6", ".6....28.", "...419..5", "....8..79"};
    @Test void valid() { assertTrue(new ValidSudoku().isValidSudoku(b(VALID))); }
    @Test void boxConflict() {
        String[] r = VALID.clone();
        r[0] = "83..7....";
        r[3] = "....6...3"; // remove the column clash so only the box rule fires
        r[2] = "..8....6.";
        assertFalse(new ValidSudoku().isValidSudoku(b(r)));
    }
    @Test void rowConflict() {
        String[] r = VALID.clone();
        r[0] = "53..7..5.";
        assertFalse(new ValidSudoku().isValidSudoku(b(r)));
    }
}
