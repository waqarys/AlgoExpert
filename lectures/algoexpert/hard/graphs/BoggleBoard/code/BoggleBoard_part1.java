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
