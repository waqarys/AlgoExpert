package advancedgraphs;

import java.util.*;

/**
 * LC 332 Reconstruct Itinerary.
 * Approach: Hierholzer's algorithm with min-heaps for lexical order; post-order prepend.
 * Time O(E log E), Space O(E).
 */
public class ReconstructItinerary {
    private final Map<String, PriorityQueue<String>> g = new HashMap<>();
    private final LinkedList<String> route = new LinkedList<>();

    public List<String> findItinerary(List<List<String>> tickets) {
        for (List<String> t : tickets) g.computeIfAbsent(t.get(0), k -> new PriorityQueue<>()).add(t.get(1));
        dfs("JFK");
        return route;
    }

    private void dfs(String a) {
        PriorityQueue<String> pq = g.get(a);
        while (pq != null && !pq.isEmpty()) dfs(pq.poll());
        route.addFirst(a);
    }
}
