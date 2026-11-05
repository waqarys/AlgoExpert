package tries;

/**
 * LC 208 Implement Trie (Prefix Tree).
 * Approach: 26-way child array per node plus an end flag.
 * O(L) per operation.
 */
public class Trie {
    private static class Node {
        Node[] next = new Node[26];
        boolean end;
    }

    private final Node root = new Node();

    public void insert(String word) {
        Node n = root;
        for (char c : word.toCharArray()) {
            if (n.next[c - 'a'] == null) n.next[c - 'a'] = new Node();
            n = n.next[c - 'a'];
        }
        n.end = true;
    }

    public boolean search(String word) {
        Node n = find(word);
        return n != null && n.end;
    }

    public boolean startsWith(String prefix) { return find(prefix) != null; }

    private Node find(String s) {
        Node n = root;
        for (char c : s.toCharArray()) {
            n = n.next[c - 'a'];
            if (n == null) return null;
        }
        return n;
    }
}
