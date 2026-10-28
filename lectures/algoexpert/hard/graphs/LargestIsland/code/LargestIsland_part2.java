            best = Math.max(best, s);
        }
        for (int r = 0; r < R; r++) for (int c = 0; c < C; c++) {
            if (m[r][c] != 1) continue;
            Set<Integer> ids = new HashSet<>();
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nc >= 0 && nr < R && nc < C && m[nr][nc] > 1) ids.add(m[nr][nc]);
            }
            int s = 1;
            for (int i : ids) s += size.get(i);
            best = Math.max(best, s);
        }
        return best;
    }
}
