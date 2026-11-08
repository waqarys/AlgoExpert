package backtracking;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class CombinationSumTest {
    CombinationSum s = new CombinationSum();
    @Test void examples() {
        assertEquals(List.of(List.of(2, 2, 3), List.of(7)), s.combinationSum(new int[]{2, 3, 6, 7}, 7));
        assertEquals(List.of(List.of(2, 2, 2, 2), List.of(2, 3, 3), List.of(3, 5)), s.combinationSum(new int[]{2, 3, 5}, 8));
        assertEquals(List.of(), s.combinationSum(new int[]{2}, 1));
    }
}
