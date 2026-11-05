package stack;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class EvaluateReversePolishNotationTest {
    EvaluateReversePolishNotation s = new EvaluateReversePolishNotation();
    @Test void examples() {
        assertEquals(9, s.evalRPN(new String[]{"2", "1", "+", "3", "*"}));
        assertEquals(6, s.evalRPN(new String[]{"4", "13", "5", "/", "+"}));
        assertEquals(22, s.evalRPN(new String[]{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}));
    }
    @Test void truncation() { assertEquals(-2, s.evalRPN(new String[]{"-7", "3", "/"})); }
}
