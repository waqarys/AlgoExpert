package binarysearch;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TimeMapTest {
    @Test void example() {
        TimeMap t = new TimeMap();
        t.set("foo", "bar", 1);
        assertEquals("bar", t.get("foo", 1));
        assertEquals("bar", t.get("foo", 3));
        t.set("foo", "bar2", 4);
        assertEquals("bar2", t.get("foo", 4));
        assertEquals("bar2", t.get("foo", 5));
        assertEquals("", t.get("foo", 0));
        assertEquals("", t.get("nope", 9));
    }
}
