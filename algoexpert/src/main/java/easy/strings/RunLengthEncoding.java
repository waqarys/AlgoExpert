package easy.strings;

/**
 * Run-Length Encoding: encode runs as count+char, with runs longer than 9 split ("AAAAAAAAAAAA" -> "9A3A").
 * Time: O(n) | Space: O(n).
 */
public class RunLengthEncoding {
    public static String runLengthEncoding(String s) {
        StringBuilder sb = new StringBuilder();
        int run = 1;
        for (int i = 1; i <= s.length(); i++) {
            if (i == s.length() || s.charAt(i) != s.charAt(i - 1) || run == 9) {
                sb.append(run).append(s.charAt(i - 1));
                run = 1;
            } else run++;
        }
        return sb.toString();
    }
}
