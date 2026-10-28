public class SearchInSortedMatrix {
    public static int[] searchInSortedMatrix(int[][] m, int target) {
        int r = 0, c = m[0].length - 1;
        while (r < m.length && c >= 0) {
            if (m[r][c] == target) return new int[]{r, c};
            if (m[r][c] > target) c--; else r++;
        }
        return new int[]{-1, -1};
    }
}
