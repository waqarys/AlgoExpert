public class GroupAnagrams {
    public static List<List<String>> groupAnagrams(List<String> words) {
        Map<String, List<String>> groups = new LinkedHashMap<>();
        for (String w : words) {
            char[] c = w.toCharArray();
            Arrays.sort(c);
            groups.computeIfAbsent(new String(c), k -> new ArrayList<>()).add(w);
        }
        return new ArrayList<>(groups.values());
    }
}
