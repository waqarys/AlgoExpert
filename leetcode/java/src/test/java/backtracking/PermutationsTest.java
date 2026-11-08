package backtracking;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class PermutationsTest {
    @Test void examples() {
        assertEquals(List.of(List.of(1, 2, 3), List.of(1, 3, 2), List.of(2, 1, 3), List.of(2, 3, 1), List.of(3, 1, 2), List.of(3, 2, 1)),
                new Permutations().permute(new int[]{1, 2, 3}));
        assertEquals(List.of(List.of(1)), new Permutations().permute(new int[]{1}));
        assertEquals(24, new Permutations().permute(new int[]{1, 2, 3, 4}).size());
    }
}
