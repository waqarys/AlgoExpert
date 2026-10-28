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
