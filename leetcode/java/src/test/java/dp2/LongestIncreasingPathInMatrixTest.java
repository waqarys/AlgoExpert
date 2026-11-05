package dp2;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LongestIncreasingPathInMatrixTest {
    LongestIncreasingPathInMatrix s = new LongestIncreasingPathInMatrix();
    @Test void examples() {
        assertEquals(4, s.longestIncreasingPath(new int[][]{{9, 9, 4}, {6, 6, 8}, {2, 1, 1}}));
        assertEquals(4, s.longestIncreasingPath(new int[][]{{3, 4, 5}, {3, 2, 6}, {2, 2, 1}}));
        assertEquals(1, s.longestIncreasingPath(new int[][]{{1}}));
    }
}
