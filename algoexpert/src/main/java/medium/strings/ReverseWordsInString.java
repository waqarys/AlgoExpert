package medium.strings;

/**
 * Reverse Words In String: reverse the order of space-separated words, preserving all whitespace runs.
 * Time: O(n) | Space: O(n).
 */
public class ReverseWordsInString {
    public static String reverseWordsInString(String s) {
        StringBuilder out = new StringBuilder();
        int end = s.length();
        for (int i = s.length() - 1; i >= -1; i--) {
            if (i == -1 || (s.charAt(i) == ' ') != (s.charAt(end - 1) == ' ')) {
                out.append(s, i + 1, end);
                end = i + 1;
            }
            if (end == 0) break;
        }
        return out.toString();
    }
}
