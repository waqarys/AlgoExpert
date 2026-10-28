package hard.tries;

import java.util.*;

/**
 * Multi String Search: for each small string, does it occur in the big string? Trie of small strings,
 * scanned from every start position of the big string.
 * Time: O(ns + bs) where b is the big length, s the longest small | Space: O(ns).
 */
public class MultiStringSearch {
    private static class Trie { Map<Character, Trie> next = new HashMap<>(); String word; }

    public static List<Boolean> multiStringSearch(String big, String[] smalls) {
        Trie root = new Trie();
        for (String s : smalls) {
            Trie t = root;
            for (char c : s.toCharArray()) t = t.next.computeIfAbsent(c, k -> new Trie());
            t.word = s;
        }
        Set<String> found = new HashSet<>();
        for (int i = 0; i < big.length(); i++) {
            Trie t = root;
            for (int j = i; j < big.length(); j++) {
                t = t.next.get(big.charAt(j));
                if (t == null) break;
                if (t.word != null) found.add(t.word);
            }
        }
        List<Boolean> out = new ArrayList<>();
        for (String s : smalls) out.add(found.contains(s));
        return out;
    }
}
