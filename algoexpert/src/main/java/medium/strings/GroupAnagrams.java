package medium.strings;

import java.util.*;

/**
 * Group Anagrams: group words that are anagrams of each other (key = sorted letters).
 * Time: O(w * n log n) | Space: O(w * n).
 */
public class GroupAnagrams {
    public static List<List<String>> groupAnagrams(List<String> words) {
        Map<String, List<String>> groups = new LinkedHashMap<>();
        for (String w : words) {
            char[] c = w.toCharArray();
            Arrays.sort(c);
            groups.computeIfAbsent(new String(c), k -> new ArrayList<>()).add(w);
        }
        return new ArrayList<>(groups.values());
    }
}
