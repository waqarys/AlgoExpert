package math;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SetMatrixZeroesTest {
    @Test void examples() {
        int[][] a = {{1, 1, 1}, {1, 0, 1}, {1, 1, 1}};
        new SetMatrixZeroes().setZeroes(a);
        assertArrayEquals(new int[][]{{1, 0, 1}, {0, 0, 0}, {1, 0, 1}}, a);
        int[][] b = {{0, 1, 2, 0}, {3, 4, 5, 2}, {1, 3, 1, 5}};
        new SetMatrixZeroes().setZeroes(b);
        assertArrayEquals(new int[][]{{0, 0, 0, 0}, {0, 4, 5, 0}, {0, 3, 1, 0}}, b);
    }
}
