public class SuffixTrieConstruction {
    public static class TrieNode { public final Map<Character, TrieNode> children = new HashMap<>(); }

    public static class SuffixTrie {
        public final TrieNode root = new TrieNode();
        private static final char END = '*';

        public SuffixTrie(String s) {
            for (int i = 0; i < s.length(); i++) {
                TrieNode n = root;
                for (int j = i; j < s.length(); j++) n = n.children.computeIfAbsent(s.charAt(j), k -> new TrieNode());
                n.children.put(END, null);
            }
        }

        public boolean contains(String s) {
            TrieNode n = root;
            for (char c : s.toCharArray()) { n = n.children.get(c); if (n == null) return false; }
            return n.children.containsKey(END);
        }
    }
}
