package tries;

/**
 * LC 211 Design Add and Search Words Data Structure.
 * Approach: trie; '.' explores all children via DFS.
 * add O(L), search O(26^dots * L) worst case.
 */
public class WordDictionary {
    private static class Node {
        Node[] next = new Node[26];
        boolean end;
    }

    private final Node root = new Node();

    public void addWord(String word) {
        Node n = root;
        for (char c : word.toCharArray()) {
            if (n.next[c - 'a'] == null) n.next[c - 'a'] = new Node();
            n = n.next[c - 'a'];
        }
        n.end = true;
    }

    public boolean search(String word) { return dfs(root, word, 0); }

    private boolean dfs(Node n, String w, int i) {
        if (i == w.length()) return n.end;
        char c = w.charAt(i);
        if (c == '.') {
            for (Node child : n.next) if (child != null && dfs(child, w, i + 1)) return true;
            return false;
        }
        Node child = n.next[c - 'a'];
        return child != null && dfs(child, w, i + 1);
    }
}
