package tries;

import java.util.*;

/**
 * LC 212 Word Search II.
 * Approach: trie of words + grid backtracking that follows trie edges; prune dead prefixes.
 * Time O(mn * 4 * 3^(L-1)) worst case, Space O(total chars).
 */
public class WordSearchII {
    private static class Node {
        Node[] next = new Node[26];
        String word;
    }

    public List<String> findWords(char[][] board, String[] words) {
        Node root = new Node();
        for (String w : words) {
            Node n = root;
            for (char c : w.toCharArray()) {
                if (n.next[c - 'a'] == null) n.next[c - 'a'] = new Node();
                n = n.next[c - 'a'];
            }
            n.word = w;
        }
        List<String> res = new ArrayList<>();
        for (int r = 0; r < board.length; r++)
            for (int c = 0; c < board[0].length; c++) dfs(board, r, c, root, res);
        return res;
    }

    private void dfs(char[][] b, int r, int c, Node parent, List<String> res) {
        if (r < 0 || c < 0 || r >= b.length || c >= b[0].length || b[r][c] == '#') return;
        char ch = b[r][c];
        Node n = parent.next[ch - 'a'];
        if (n == null) return;
        if (n.word != null) { res.add(n.word); n.word = null; }
        b[r][c] = '#';
        dfs(b, r + 1, c, n, res);
        dfs(b, r - 1, c, n, res);
        dfs(b, r, c + 1, n, res);
        dfs(b, r, c - 1, n, res);
        b[r][c] = ch;
    }
}
