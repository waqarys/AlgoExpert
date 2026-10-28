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
