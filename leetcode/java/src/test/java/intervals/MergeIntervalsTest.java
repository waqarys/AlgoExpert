package intervals;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MergeIntervalsTest {
    MergeIntervals s = new MergeIntervals();
    @Test void examples() {
        assertArrayEquals(new int[][]{{1, 6}, {8, 10}, {15, 18}}, s.merge(new int[][]{{1, 3}, {2, 6}, {8, 10}, {15, 18}}));
        assertArrayEquals(new int[][]{{1, 5}}, s.merge(new int[][]{{1, 4}, {4, 5}}));
        assertArrayEquals(new int[][]{{1, 10}}, s.merge(new int[][]{{2, 3}, {1, 10}}));
    }
}
