    private static Map<String, Integer> tarjan(List<String> nodes, Map<String, List<String>> g) {
        Map<String, Integer> idx = new HashMap<>(), low = new HashMap<>(), comp = new HashMap<>();
        Deque<String> st = new ArrayDeque<>();
        Set<String> on = new HashSet<>();
        int[] counter = {0, 0};
        for (String n : nodes) if (!idx.containsKey(n)) strong(n, g, idx, low, comp, st, on, counter);
        return comp;
    }
