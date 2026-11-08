package advancedgraphs;

import java.util.*;

/**
 * LC 269 Alien Dictionary.
 * Approach: edges from first differing letters of adjacent words, then Kahn's topological sort.
 * Time O(total chars), Space O(alphabet + edges).
 */
public class AlienDictionary {
    public String alienOrder(String[] words) {
        Map<Character, Set<Character>> adj = new LinkedHashMap<>();
        Map<Character, Integer> indeg = new HashMap<>();
        for (String w : words)
            for (char c : w.toCharArray()) { adj.putIfAbsent(c, new LinkedHashSet<>()); indeg.putIfAbsent(c, 0); }
        for (int i = 0; i + 1 < words.length; i++) {
            String a = words[i], b = words[i + 1];
            int len = Math.min(a.length(), b.length()), j = 0;
            while (j < len && a.charAt(j) == b.charAt(j)) j++;
            if (j == len) {
                if (a.length() > b.length()) return "";
                continue;
            }
            if (adj.get(a.charAt(j)).add(b.charAt(j))) indeg.merge(b.charAt(j), 1, Integer::sum);
        }
        Deque<Character> q = new ArrayDeque<>();
        for (char c : adj.keySet()) if (indeg.get(c) == 0) q.add(c);
        StringBuilder sb = new StringBuilder();
        while (!q.isEmpty()) {
            char c = q.poll();
            sb.append(c);
            for (char nx : adj.get(c)) if (indeg.merge(nx, -1, Integer::sum) == 0) q.add(nx);
        }
        return sb.length() == adj.size() ? sb.toString() : "";
    }
}
