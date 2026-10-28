public class MultiStringSearch {
    private static class Trie { Map<Character, Trie> next = new HashMap<>(); String word; }

    public static List<Boolean> multiStringSearch(String big, String[] smalls) {
        Trie root = new Trie();
        for (String s : smalls) {
            Trie t = root;
            for (char c : s.toCharArray()) t = t.next.computeIfAbsent(c, k -> new Trie());
            t.word = s;
        }
        Set<String> found = new HashSet<>();
        for (int i = 0; i < big.length(); i++) {
            Trie t = root;
            for (int j = i; j < big.length(); j++) {
                t = t.next.get(big.charAt(j));
                if (t == null) break;
                if (t.word != null) found.add(t.word);
            }
        }
        List<Boolean> out = new ArrayList<>();
        for (String s : smalls) out.add(found.contains(s));
        return out;
    }
