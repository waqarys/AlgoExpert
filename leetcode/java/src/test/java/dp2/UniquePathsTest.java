package dp2;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class UniquePathsTest {
    UniquePaths s = new UniquePaths();
    @Test void examples() {
        assertEquals(28, s.uniquePaths(3, 7));
        assertEquals(3, s.uniquePaths(3, 2));
        assertEquals(1, s.uniquePaths(1, 1));
        assertEquals(1, s.uniquePaths(1, 10));
    }
}
