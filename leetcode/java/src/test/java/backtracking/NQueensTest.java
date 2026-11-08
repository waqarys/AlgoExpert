package backtracking;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class NQueensTest {
    NQueens s = new NQueens();
    @Test void examples() {
        assertEquals(List.of(List.of(".Q..", "...Q", "Q...", "..Q."), List.of("..Q.", "Q...", "...Q", ".Q..")), s.solveNQueens(4));
        assertEquals(List.of(List.of("Q")), s.solveNQueens(1));
        assertEquals(92, s.solveNQueens(8).size());
        assertEquals(0, s.solveNQueens(3).size());
    }
}
