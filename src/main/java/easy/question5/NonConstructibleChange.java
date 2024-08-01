package easy.question5;

import java.util.Arrays;

/**
 *
 * Create a variable to store the amount of change that you can currently create
 * up to. Sort all of your coins, and loop through them in ascending order. At
 * every iteration, compare the current coin to the amount of change that you can
 * currently create up to. Here are the two scenarios that you'll encounter:
 * <ul>
 *   <li>
 *     The coin value is <b>greater</b> than the amount of change that you can
 *     currently create plus 1.
 *   </li>
 *   <li>
 *     The coin value is <b>smaller than or equal to</b> the amount of change that
 *     you can currently create plus 1.
 *   </li>
 * </ul>
 *
 * In the first scenario, you simply return the current amount of change that you
 * can create plus 1, because you can't create that amount of change. In the
 * second scenario, you add the value of the coin to the amount of change that
 * you can currently create up to, and you continue iterating through the coins.
 */
public class NonConstructibleChange {

    public static void main(String[] args) {
        int[] input = new int[] {5, 7, 1, 1, 2, 3, 22};
        int expected = 20;
        var actual = new NonConstructibleChange().nonConstructibleChange(input);
        System.out.println(expected == actual);
    }

    public int nonConstructibleChange(int[] coins) {
        Arrays.sort(coins);

        int currentChangeCreated = 0;
        for(int coin: coins) {
            if(coin > currentChangeCreated + 1){
                return currentChangeCreated + 1;
            }

            currentChangeCreated += coin;
        }
        return currentChangeCreated + 1;
    }
}
