package stack;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class GenerateParenthesesTest {
    GenerateParentheses s = new GenerateParentheses();
    @Test void examples() {
        assertEquals(List.of("((()))", "(()())", "(())()", "()(())", "()()()"), s.generateParenthesis(3));
        assertEquals(List.of("()"), s.generateParenthesis(1));
        assertEquals(14, s.generateParenthesis(4).size());
    }
}
