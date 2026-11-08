package backtracking;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class SubsetsIITest {
    @Test void examples() {
        assertEquals(List.of(List.of(), List.of(1), List.of(1, 2), List.of(1, 2, 2), List.of(2), List.of(2, 2)),
                new SubsetsII().subsetsWithDup(new int[]{1, 2, 2}));
        assertEquals(List.of(List.of(), List.of(0)), new SubsetsII().subsetsWithDup(new int[]{0}));
        assertEquals(10, new SubsetsII().subsetsWithDup(new int[]{4, 4, 4, 1, 4}).size());
    }
}
