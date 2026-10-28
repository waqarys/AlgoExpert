package easy.strings;

import java.util.HashMap;
import java.util.Map;

/**
 * Generate Document: can `document` be built from the multiset of characters in `characters`?
 * Time: O(n + m) | Space: O(c).
 */
public class GenerateDocument {
    public static boolean generateDocument(String characters, String document) {
        Map<Character, Integer> counts = new HashMap<>();
        for (char c : characters.toCharArray()) counts.merge(c, 1, Integer::sum);
        for (char c : document.toCharArray()) {
            int left = counts.getOrDefault(c, 0);
            if (left == 0) return false;
            counts.put(c, left - 1);
        }
        return true;
    }
}
