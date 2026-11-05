package stack;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MinStackTest {
    @Test void example() {
        MinStack m = new MinStack();
        m.push(-2); m.push(0); m.push(-3);
        assertEquals(-3, m.getMin());
        m.pop();
        assertEquals(0, m.top());
        assertEquals(-2, m.getMin());
    }
    @Test void duplicateMins() {
        MinStack m = new MinStack();
        m.push(1); m.push(1); m.pop();
        assertEquals(1, m.getMin());
    }
}
