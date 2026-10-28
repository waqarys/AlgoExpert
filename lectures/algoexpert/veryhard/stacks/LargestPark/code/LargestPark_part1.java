public class LargestPark {
    public static int largestPark(boolean[][] land) {
        if (land.length == 0) return 0;
        int[] heights = new int[land[0].length];
        int best = 0;
        for (boolean[] row : land) {
            for (int c = 0; c < row.length; c++) heights[c] = row[c] ? 0 : heights[c] + 1;
            best = Math.max(best, largestRectangle(heights));
        }
        return best;
    }
