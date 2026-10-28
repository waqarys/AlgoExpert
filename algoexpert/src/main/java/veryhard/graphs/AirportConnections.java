package veryhard.graphs;

import java.util.*;

/**
 * Airport Connections: minimum number of new one-way routes from the starting airport so every airport is
 * reachable. Collapse strongly connected components (Tarjan) and count SCCs with in-degree 0, excluding
 * the one containing the start.
 * Time: O(a + r) | Space: O(a + r).
 */
public class AirportConnections {
    public static int airportConnections(List<String> airports, List<List<String>> routes, String start) {
        Map<String, List<String>> g = new HashMap<>();
        for (String a : airports) g.put(a, new ArrayList<>());
        for (List<String> r : routes) g.get(r.get(0)).add(r.get(1));
        Map<String, Integer> comp = tarjan(airports, g);
        Set<Integer> hasIncoming = new HashSet<>();
        for (List<String> r : routes) {
            int a = comp.get(r.get(0)), b = comp.get(r.get(1));
            if (a != b) hasIncoming.add(b);
        }
        Set<Integer> all = new HashSet<>(comp.values());
        int count = 0;
        for (int c : all) if (!hasIncoming.contains(c) && c != comp.get(start)) count++;
        return count;
    }

    private static Map<String, Integer> tarjan(List<String> nodes, Map<String, List<String>> g) {
        Map<String, Integer> idx = new HashMap<>(), low = new HashMap<>(), comp = new HashMap<>();
        Deque<String> st = new ArrayDeque<>();
        Set<String> on = new HashSet<>();
        int[] counter = {0, 0};
        for (String n : nodes) if (!idx.containsKey(n)) strong(n, g, idx, low, comp, st, on, counter);
        return comp;
    }

    private static void strong(String v, Map<String, List<String>> g, Map<String, Integer> idx, Map<String, Integer> low,
                               Map<String, Integer> comp, Deque<String> st, Set<String> on, int[] counter) {
        idx.put(v, counter[0]); low.put(v, counter[0]); counter[0]++;
        st.push(v); on.add(v);
        for (String w : g.get(v)) {
            if (!idx.containsKey(w)) { strong(w, g, idx, low, comp, st, on, counter); low.put(v, Math.min(low.get(v), low.get(w))); }
            else if (on.contains(w)) low.put(v, Math.min(low.get(v), idx.get(w)));
        }
        if (low.get(v).equals(idx.get(v))) {
            String w;
            do { w = st.pop(); on.remove(w); comp.put(w, counter[1]); } while (!w.equals(v));
            counter[1]++;
        }
    }
}
