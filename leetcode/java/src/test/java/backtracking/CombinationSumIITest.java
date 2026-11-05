package backtracking;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class CombinationSumIITest {
    CombinationSumII s = new CombinationSumII();
    @Test void examples() {
        assertEquals(List.of(List.of(1, 1, 6), List.of(1, 2, 5), List.of(1, 7), List.of(2, 6)),
                s.combinationSum2(new int[]{10, 1, 2, 7, 6, 1, 5}, 8));
        assertEquals(List.of(List.of(1, 2, 2), List.of(5)), s.combinationSum2(new int[]{2, 5, 2, 1, 2}, 5));
    }
}
