package hard.graphs;

import java.util.*;

/**
 * Boggle Board: which words can be formed by chaining 8-directionally adjacent letters without reusing a
 * cell? Trie of words + DFS from every cell.
 * Time: O(ws + w*h*8^s) | Space: O(ws + w*h).
 */
public class BoggleBoard {
    private static class Trie { Map<Character, Trie> next = new HashMap<>(); String word; }

    public static List<String> boggleBoard(char[][] board, String[] words) {
        Trie root = new Trie();
        for (String w : words) {
            Trie t = root;
            for (char c : w.toCharArray()) t = t.next.computeIfAbsent(c, k -> new Trie());
            t.word = w;
        }
        Set<String> found = new LinkedHashSet<>();
        boolean[][] used = new boolean[board.length][board[0].length];
        for (int r = 0; r < board.length; r++) for (int c = 0; c < board[0].length; c++) dfs(board, r, c, root, used, found);
        return new ArrayList<>(found);
    }

    private static void dfs(char[][] b, int r, int c, Trie t, boolean[][] used, Set<String> found) {
        if (r < 0 || c < 0 || r >= b.length || c >= b[0].length || used[r][c]) return;
        Trie nx = t.next.get(b[r][c]);
        if (nx == null) return;
        if (nx.word != null) found.add(nx.word);
        used[r][c] = true;
        for (int dr = -1; dr <= 1; dr++) for (int dc = -1; dc <= 1; dc++) if (dr != 0 || dc != 0) dfs(b, r + dr, c + dc, nx, used, found);
        used[r][c] = false;
    }
}
