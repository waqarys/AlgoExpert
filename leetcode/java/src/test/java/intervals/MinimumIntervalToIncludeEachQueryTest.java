package intervals;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MinimumIntervalToIncludeEachQueryTest {
    MinimumIntervalToIncludeEachQuery s = new MinimumIntervalToIncludeEachQuery();
    @Test void examples() {
        assertArrayEquals(new int[]{3, 3, 1, 4}, s.minInterval(new int[][]{{1, 4}, {2, 4}, {3, 6}, {4, 4}}, new int[]{2, 3, 4, 5}));
        assertArrayEquals(new int[]{2, -1, 4, 6}, s.minInterval(new int[][]{{2, 3}, {2, 5}, {1, 8}, {20, 25}}, new int[]{2, 19, 5, 22}));
    }
}
