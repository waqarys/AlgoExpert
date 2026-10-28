                if (g[r][c] + 1 < g[nr][nc]) {
                    g[nr][nc] = g[r][c] + 1;
                    from[nr * C + nc] = new int[]{r, c};
                    open.add(new int[]{nr, nc, g[nr][nc] + h(nr, nc, endRow, endCol)});
                }
            }
        }
        return new int[][]{};
    }

    private static int h(int r, int c, int er, int ec) { return Math.abs(r - er) + Math.abs(c - ec); }
}
