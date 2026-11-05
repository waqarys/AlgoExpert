package linkedlist;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LRUCacheTest {
    @Test void example() {
        LRUCache c = new LRUCache(2);
        c.put(1, 1); c.put(2, 2);
        assertEquals(1, c.get(1));
        c.put(3, 3);
        assertEquals(-1, c.get(2));
        c.put(4, 4);
        assertEquals(-1, c.get(1));
        assertEquals(3, c.get(3));
        assertEquals(4, c.get(4));
    }
    @Test void updateRefreshes() {
        LRUCache c = new LRUCache(2);
        c.put(1, 1); c.put(2, 2); c.put(1, 10); c.put(3, 3);
        assertEquals(10, c.get(1));
        assertEquals(-1, c.get(2));
    }
}
