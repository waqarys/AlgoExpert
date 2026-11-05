package greedy;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ValidParenthesisStringTest {
    ValidParenthesisString s = new ValidParenthesisString();
    @Test void examples() {
        assertTrue(s.checkValidString("()"));
        assertTrue(s.checkValidString("(*)"));
        assertTrue(s.checkValidString("(*))"));
        assertFalse(s.checkValidString("(("));
        assertFalse(s.checkValidString("*)("));
        assertFalse(s.checkValidString(")*"));
    }
}
