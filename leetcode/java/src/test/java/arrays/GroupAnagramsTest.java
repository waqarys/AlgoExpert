package arrays;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class GroupAnagramsTest {
    static Set<Set<String>> norm(List<List<String>> g) {
        Set<Set<String>> out = new HashSet<>();
        for (List<String> l : g) out.add(new HashSet<>(l));
        return out;
    }
    @Test void example() {
        var r = new GroupAnagrams().groupAnagrams(new String[]{"eat", "tea", "tan", "ate", "nat", "bat"});
        assertEquals(Set.of(Set.of("bat"), Set.of("nat", "tan"), Set.of("ate", "eat", "tea")), norm(r));
    }
    @Test void edges() {
        assertEquals(List.of(List.of("")), new GroupAnagrams().groupAnagrams(new String[]{""}));
        assertEquals(List.of(List.of("a")), new GroupAnagrams().groupAnagrams(new String[]{"a"}));
    }
}
