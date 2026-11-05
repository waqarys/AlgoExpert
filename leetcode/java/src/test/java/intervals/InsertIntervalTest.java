package intervals;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class InsertIntervalTest {
    InsertInterval s = new InsertInterval();
    @Test void examples() {
        assertArrayEquals(new int[][]{{1, 5}, {6, 9}}, s.insert(new int[][]{{1, 3}, {6, 9}}, new int[]{2, 5}));
        assertArrayEquals(new int[][]{{1, 2}, {3, 10}, {12, 16}},
                s.insert(new int[][]{{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}}, new int[]{4, 8}));
        assertArrayEquals(new int[][]{{5, 7}}, s.insert(new int[][]{}, new int[]{5, 7}));
        assertArrayEquals(new int[][]{{1, 7}}, s.insert(new int[][]{{1, 5}}, new int[]{5, 7}));
    }
}
