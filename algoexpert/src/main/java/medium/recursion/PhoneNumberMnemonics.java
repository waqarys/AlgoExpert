package medium.recursion;

import java.util.ArrayList;
import java.util.List;

/**
 * Phone Number Mnemonics: all letter strings a digit string could spell on a keypad (0 and 1 map to themselves).
 * Time: O(4^n * n) | Space: O(4^n * n).
 */
public class PhoneNumberMnemonics {
    private static final String[] KEYS = {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public static List<String> phoneNumberMnemonics(String phone) {
        List<String> out = new ArrayList<>();
        build(phone, 0, new StringBuilder(), out);
        return out;
    }

    private static void build(String p, int i, StringBuilder sb, List<String> out) {
        if (i == p.length()) { out.add(sb.toString()); return; }
        for (char c : KEYS[p.charAt(i) - '0'].toCharArray()) { sb.append(c); build(p, i + 1, sb, out); sb.setLength(sb.length() - 1); }
    }
}
