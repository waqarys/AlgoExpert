package backtracking;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class LetterCombinationsOfPhoneNumberTest {
    LetterCombinationsOfPhoneNumber s = new LetterCombinationsOfPhoneNumber();
    @Test void examples() {
        assertEquals(List.of("ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"), s.letterCombinations("23"));
        assertEquals(List.of(), s.letterCombinations(""));
        assertEquals(List.of("a", "b", "c"), s.letterCombinations("2"));
        assertEquals(16, s.letterCombinations("79").size());
    }
}
