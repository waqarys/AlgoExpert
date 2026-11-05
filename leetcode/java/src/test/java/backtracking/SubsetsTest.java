package backtracking;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class SubsetsTest {
    @Test void examples() {
        assertEquals(List.of(List.of(), List.of(1), List.of(1, 2), List.of(1, 2, 3), List.of(1, 3), List.of(2), List.of(2, 3), List.of(3)),
                new Subsets().subsets(new int[]{1, 2, 3}));
        assertEquals(List.of(List.of(), List.of(0)), new Subsets().subsets(new int[]{0}));
    }
}
