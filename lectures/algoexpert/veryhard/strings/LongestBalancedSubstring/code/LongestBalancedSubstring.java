public class LongestBalancedSubstring {
    public static int longestBalancedSubstring(String s) {
        return Math.max(scan(s, false), scan(s, true));
    }

    private static int scan(String s, boolean reverse) {
        int open = 0, close = 0, best = 0;
        for (int k = 0; k < s.length(); k++) {
            char c = s.charAt(reverse ? s.length() - 1 - k : k);
            boolean opening = (c == '(') != reverse;
            if (opening) open++; else close++;
            if (open == close) best = Math.max(best, 2 * close);
            else if (close > open) open = close = 0;
        }
        return best;
    }
}
