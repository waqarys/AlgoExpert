package backtracking;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class PalindromePartitioningTest {
    @Test void examples() {
        var s = new PalindromePartitioning();
        assertEquals(List.of(List.of("a", "a", "b"), List.of("aa", "b")), s.partition("aab"));
        assertEquals(List.of(List.of("a")), s.partition("a"));
        assertEquals(List.of(List.of("a", "b", "a"), List.of("aba")), s.partition("aba"));
    }
}
