public class Semordnilap {
    public static List<List<String>> semordnilap(String[] words) {
        Set<String> set = new HashSet<>(Arrays.asList(words));
        List<List<String>> out = new ArrayList<>();
        for (String w : words) {
            String r = new StringBuilder(w).reverse().toString();
            if (!r.equals(w) && set.contains(r)) {
                out.add(List.of(w, r));
                set.remove(w);
                set.remove(r);
            }
        }
        return out;
    }
}
