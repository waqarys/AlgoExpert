package medium.strings;

import java.util.ArrayList;
import java.util.List;
import java.util.TreeMap;

/**
 * Minimum Characters For Words: smallest multiset of characters that can spell each word (one at a time).
 * Time: O(n * l) | Space: O(c).
 */
public class MinimumCharactersForWords {
    public static char[] minimumCharactersForWords(String[] words) {
        TreeMap<Character, Integer> need = new TreeMap<>();
        for (String w : words) {
            TreeMap<Character, Integer> f = new TreeMap<>();
            for (char c : w.toCharArray()) f.merge(c, 1, Integer::sum);
            f.forEach((c, n) -> need.merge(c, n, Math::max));
        }
        List<Character> out = new ArrayList<>();
        need.forEach((c, n) -> { for (int i = 0; i < n; i++) out.add(c); });
        char[] r = new char[out.size()];
        for (int i = 0; i < r.length; i++) r[i] = out.get(i);
        return r;
    }
}
