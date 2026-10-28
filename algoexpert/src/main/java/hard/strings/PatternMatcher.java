package hard.strings;

/**
 * Pattern Matcher: pattern of 'x'/'y'; find substrings x and y so substituting yields `str`.
 * Returns [x, y] (empty strings if unused) or [] if impossible. Normalise so pattern starts with 'x',
 * then try every length of x.
 * Time: O(n^2 + m) | Space: O(n + m).
 */
public class PatternMatcher {
    public static String[] patternMatcher(String pattern, String str) {
        if (pattern.length() > str.length()) return new String[]{};
        boolean swapped = pattern.charAt(0) != 'x';
        String p = swapped ? pattern.replace('x', '#').replace('y', 'x').replace('#', 'y') : pattern;
        int cx = 0, cy = 0, firstY = -1;
        for (int i = 0; i < p.length(); i++) {
            if (p.charAt(i) == 'x') cx++; else { cy++; if (firstY == -1) firstY = i; }
        }
        for (int lx = 1; lx * cx <= str.length(); lx++) {
            int rest = str.length() - lx * cx;
            if (cy == 0 ? rest != 0 : rest % cy != 0) continue;
            int ly = cy == 0 ? 0 : rest / cy;
            String x = str.substring(0, lx);
            String y = cy == 0 ? "" : str.substring(firstY * lx, firstY * lx + ly);
            StringBuilder sb = new StringBuilder();
            for (char c : p.toCharArray()) sb.append(c == 'x' ? x : y);
            if (sb.toString().equals(str)) return swapped ? new String[]{y, x} : new String[]{x, y};
        }
        return new String[]{};
    }
}
