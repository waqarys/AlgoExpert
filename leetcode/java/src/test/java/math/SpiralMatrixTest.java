package math;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class SpiralMatrixTest {
    SpiralMatrix s = new SpiralMatrix();
    @Test void examples() {
        assertEquals(List.of(1, 2, 3, 6, 9, 8, 7, 4, 5), s.spiralOrder(new int[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}));
        assertEquals(List.of(1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7), s.spiralOrder(new int[][]{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}}));
        assertEquals(List.of(1, 2, 3), s.spiralOrder(new int[][]{{1}, {2}, {3}}));
    }
}
