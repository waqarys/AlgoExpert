package hard.strings;

import java.util.HashMap;
import java.util.Map;

/**
 * Longest Substring Without Duplication: sliding window with last-seen index per character.
 * Time: O(n) | Space: O(min(n, a)).
 */
public class LongestSubstringWithoutDuplication {
    public static String longestSubstringWithoutDuplication(String s) {
        Map<Character, Integer> last = new HashMap<>();
        int start = 0, bs = 0, be = 0;
        for (int i = 0; i < s.length(); i++) {
            Integer p = last.get(s.charAt(i));
            if (p != null && p >= start) start = p + 1;
            last.put(s.charAt(i), i);
            if (i + 1 - start > be - bs) { bs = start; be = i + 1; }
        }
        return s.substring(bs, be);
    }
}
