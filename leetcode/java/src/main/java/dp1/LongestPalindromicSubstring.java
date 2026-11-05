package dp1;

/**
 * LC 5 Longest Palindromic Substring.
 * Approach: expand around each of the 2n-1 centres.
 * Time O(n^2), Space O(1).
 */
public class LongestPalindromicSubstring {
    public String longestPalindrome(String s) {
        int start = 0, best = 0;
        for (int i = 0; i < s.length(); i++) {
            int len = Math.max(expand(s, i, i), expand(s, i, i + 1));
            if (len > best) { best = len; start = i - (len - 1) / 2; }
        }
        return s.substring(start, start + best);
    }

    private int expand(String s, int l, int r) {
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) { l--; r++; }
        return r - l - 1;
    }
}
