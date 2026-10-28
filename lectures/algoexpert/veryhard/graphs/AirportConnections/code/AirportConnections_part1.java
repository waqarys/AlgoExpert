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
