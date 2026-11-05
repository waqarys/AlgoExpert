package heap;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class KClosestPointsToOriginTest {
    static Set<List<Integer>> set(int[][] pts) {
        Set<List<Integer>> s = new HashSet<>();
        for (int[] p : pts) s.add(List.of(p[0], p[1]));
        return s;
    }
    @Test void examples() {
        var s = new KClosestPointsToOrigin();
        assertEquals(Set.of(List.of(-2, 2)), set(s.kClosest(new int[][]{{1, 3}, {-2, 2}}, 1)));
        assertEquals(Set.of(List.of(3, 3), List.of(-2, 4)), set(s.kClosest(new int[][]{{3, 3}, {5, -1}, {-2, 4}}, 2)));
    }
}
