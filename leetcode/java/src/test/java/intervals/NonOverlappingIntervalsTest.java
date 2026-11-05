package intervals;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class NonOverlappingIntervalsTest {
    NonOverlappingIntervals s = new NonOverlappingIntervals();
    @Test void examples() {
        assertEquals(1, s.eraseOverlapIntervals(new int[][]{{1, 2}, {2, 3}, {3, 4}, {1, 3}}));
        assertEquals(2, s.eraseOverlapIntervals(new int[][]{{1, 2}, {1, 2}, {1, 2}}));
        assertEquals(0, s.eraseOverlapIntervals(new int[][]{{1, 2}, {2, 3}}));
    }
}
