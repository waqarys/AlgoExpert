package graphs;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CourseScheduleIITest {
    static boolean valid(int n, int[][] pre, int[] order) {
        if (order.length != n) return false;
        int[] pos = new int[n];
        for (int i = 0; i < n; i++) pos[order[i]] = i;
        for (int[] p : pre) if (pos[p[1]] > pos[p[0]]) return false;
        return true;
    }
    CourseScheduleII s = new CourseScheduleII();
    @Test void examples() {
        int[][] pre = {{1, 0}, {2, 0}, {3, 1}, {3, 2}};
        assertTrue(valid(4, pre, s.findOrder(4, pre)));
        assertArrayEquals(new int[]{0}, s.findOrder(1, new int[][]{}));
        assertArrayEquals(new int[0], s.findOrder(2, new int[][]{{0, 1}, {1, 0}}));
    }
}
