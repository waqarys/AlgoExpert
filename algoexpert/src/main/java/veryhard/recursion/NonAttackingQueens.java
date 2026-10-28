package veryhard.recursion;

/**
 * Non-Attacking Queens: number of ways to place n queens on an n x n board with no two attacking.
 * Backtracking with column/diagonal bitmasks.
 * Time: O(n!) | Space: O(n).
 */
public class NonAttackingQueens {
    public static int nonAttackingQueens(int n) { return place(n, 0, 0, 0, 0); }

    private static int place(int n, int row, int cols, int d1, int d2) {
        if (row == n) return 1;
        int count = 0;
        int free = ~(cols | d1 | d2) & ((1 << n) - 1);
        while (free != 0) {
            int bit = free & -free;
            free -= bit;
            count += place(n, row + 1, cols | bit, (d1 | bit) << 1, (d2 | bit) >> 1);
        }
        return count;
    }
}
