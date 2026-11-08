package arrays;

import java.util.*;

/**
 * LC 49 Group Anagrams.
 * Approach: canonical key = encoded 26-letter counts; bucket words in a HashMap.
 * Time O(n*k), Space O(n*k).
 */
public class GroupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();
        for (String w : strs) {
            int[] count = new int[26];
            for (char c : w.toCharArray()) count[c - 'a']++;
            StringBuilder key = new StringBuilder();
            for (int c : count) key.append('#').append(c);
            groups.computeIfAbsent(key.toString(), k -> new ArrayList<>()).add(w);
        }
        return new ArrayList<>(groups.values());
    }
}
