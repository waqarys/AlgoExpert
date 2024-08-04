package array;

public class NumberOfIslands {
    public int numIslands(char[][] grid) {
        if(grid.length == 0 || grid[0].length == 0) return 0;

        int count = 0;

        for(int r = 0; r < grid.length; r++) {
            for(int c = 0; c < grid[0].length; c++) {
                if(grid[r][c] == '1') {
                    count ++;
                    helper(grid, r, c);
                }
            }
        }
        return count;
    }

    private void helper(char[][] grid, int r, int c) {
        if(r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] == '0') return;

        grid[r][c] = '0';
        helper(grid, r + 1, c);
        helper(grid, r - 1, c);
        helper(grid, r, c + 1);
        helper(grid, r, c - 1);
    }
}
