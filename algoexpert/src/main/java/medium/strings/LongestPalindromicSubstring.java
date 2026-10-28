package medium.strings;

/**
 * Longest Palindromic Substring: expand around every centre (odd and even).
 * Time: O(n^2) | Space: O(n) output.
 */
public class LongestPalindromicSubstring {
    public static String longestPalindromicSubstring(String s) {
        int bs = 0, be = 0;
        for (int i = 0; i < s.length(); i++)
            for (int j = i; j <= i + 1; j++) {
                int l = i, r = j;
                while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) { l--; r++; }
                if (r - l - 1 > be - bs) { bs = l + 1; be = r; }
            }
        return s.substring(bs, be);
    }
}
