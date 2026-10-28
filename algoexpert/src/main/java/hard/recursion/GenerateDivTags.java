package hard.recursion;

import java.util.ArrayList;
import java.util.List;

/**
 * Generate Div Tags: all valid strings of n matched <div></div> pairs (balanced-parentheses generation).
 * Time: O(Catalan(n) * n) | Space: O(Catalan(n) * n).
 */
public class GenerateDivTags {
    public static ArrayList<String> generateDivTags(int n) {
        ArrayList<String> out = new ArrayList<>();
        gen(n, n, new StringBuilder(), out);
        return out;
    }

    private static void gen(int open, int close, StringBuilder sb, List<String> out) {
        if (close == 0) { out.add(sb.toString()); return; }
        int len = sb.length();
        if (open > 0) { sb.append("<div>"); gen(open - 1, close, sb, out); sb.setLength(len); }
        if (close > open) { sb.append("</div>"); gen(open, close - 1, sb, out); sb.setLength(len); }
    }
}
