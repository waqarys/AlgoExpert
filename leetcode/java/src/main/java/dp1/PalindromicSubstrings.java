package dp1;

/**
 * LC 647 Palindromic Substrings.
 * Approach: expand around every centre, counting each palindrome found.
 * Time O(n^2), Space O(1).
 */
public class PalindromicSubstrings {
    public int countSubstrings(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) count += expand(s, i, i) + expand(s, i, i + 1);
        return count;
    }

    private int expand(String s, int l, int r) {
        int c = 0;
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) { c++; l--; r++; }
        return c;
    }
}
