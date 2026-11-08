package greedy;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class PartitionLabelsTest {
    PartitionLabels s = new PartitionLabels();
    @Test void examples() {
        assertEquals(List.of(9, 7, 8), s.partitionLabels("ababcbacadefegdehijhklij"));
        assertEquals(List.of(10), s.partitionLabels("eccbbbbdec"));
        assertEquals(List.of(1, 1, 1), s.partitionLabels("abc"));
    }
}
