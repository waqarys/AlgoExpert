package stack;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ValidParenthesesTest {
    ValidParentheses s = new ValidParentheses();
    @Test void examples() {
        assertTrue(s.isValid("()[]{}"));
        assertFalse(s.isValid("(]"));
        assertFalse(s.isValid("([)]"));
        assertTrue(s.isValid("{[]}"));
    }
    @Test void edges() { assertFalse(s.isValid("((")); assertFalse(s.isValid("]")); assertTrue(s.isValid("")); }
}
