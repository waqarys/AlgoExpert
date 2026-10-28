package hard.dynamicprogramming;

/**
 * Dice Throws: number of ways to roll numDice dice with numSides sides to total `target`.
 * Time: O(d * t * s) | Space: O(t).
 */
public class DiceThrows {
    public static int diceThrows(int numDice, int numSides, int target) {
        long[] ways = new long[target + 1];
        ways[0] = 1;
        for (int d = 0; d < numDice; d++) {
            long[] next = new long[target + 1];
            for (int t = 0; t <= target; t++) if (ways[t] != 0)
                for (int s = 1; s <= numSides && t + s <= target; s++) next[t + s] += ways[t];
            ways = next;
        }
        return (int) ways[target];
    }
}
