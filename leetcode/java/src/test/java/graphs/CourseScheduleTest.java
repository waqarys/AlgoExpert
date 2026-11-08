package graphs;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CourseScheduleTest {
    CourseSchedule s = new CourseSchedule();
    @Test void examples() {
        assertTrue(s.canFinish(2, new int[][]{{1, 0}}));
        assertFalse(s.canFinish(2, new int[][]{{1, 0}, {0, 1}}));
        assertFalse(s.canFinish(4, new int[][]{{1, 0}, {2, 1}, {3, 2}, {1, 3}}));
        assertTrue(s.canFinish(3, new int[][]{}));
    }
}
