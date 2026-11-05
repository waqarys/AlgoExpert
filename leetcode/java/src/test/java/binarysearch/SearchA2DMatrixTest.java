package binarysearch;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SearchA2DMatrixTest {
    SearchA2DMatrix s = new SearchA2DMatrix();
    int[][] m = {{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}};
    @Test void examples() {
        assertTrue(s.searchMatrix(m, 3));
        assertFalse(s.searchMatrix(m, 13));
        assertTrue(s.searchMatrix(m, 60));
        assertFalse(s.searchMatrix(new int[][]{{1}}, 2));
    }
}
