package arrays;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class EncodeAndDecodeStringsTest {
    EncodeAndDecodeStrings c = new EncodeAndDecodeStrings();
    @Test void roundTrip() {
        List<String> in = List.of("lint", "co#de", "", "12#ab", "😀");
        assertEquals("4#lint5#co#de0#", c.encode(List.of("lint", "co#de", "")));
        assertEquals(in, c.decode(c.encode(in)));
    }
    @Test void empty() {
        assertEquals(List.of(), c.decode(c.encode(List.of())));
        assertEquals(List.of(""), c.decode(c.encode(List.of(""))));
    }
}
