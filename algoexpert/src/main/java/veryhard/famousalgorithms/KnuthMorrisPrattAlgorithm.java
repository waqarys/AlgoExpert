package veryhard.famousalgorithms;

/**
 * Knuth-Morris-Pratt Algorithm: does `sub` occur in `str`? Prefix-function (failure table) matching.
 * Time: O(n + m) | Space: O(m).
 */
public class KnuthMorrisPrattAlgorithm {
    public static boolean knuthMorrisPrattAlgorithm(String str, String sub) {
        if (sub.isEmpty()) return true;
        int[] fail = new int[sub.length()];
        for (int i = 1, k = 0; i < sub.length(); i++) {
            while (k > 0 && sub.charAt(i) != sub.charAt(k)) k = fail[k - 1];
            if (sub.charAt(i) == sub.charAt(k)) k++;
            fail[i] = k;
        }
        for (int i = 0, k = 0; i < str.length(); i++) {
            while (k > 0 && str.charAt(i) != sub.charAt(k)) k = fail[k - 1];
            if (str.charAt(i) == sub.charAt(k)) k++;
            if (k == sub.length()) return true;
        }
        return false;
    }
}
