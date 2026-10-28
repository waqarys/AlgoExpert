package medium.recursion;

import java.util.HashMap;
import java.util.Map;

/**
 * Blackjack Probability: the dealer draws cards valued 1-10 uniformly while below target-4; busts if above
 * target. Starting from a hand value, probability of busting (rounded to 3 decimals). Memoised recursion.
 * Time: O(t) | Space: O(t).
 */
public class BlackjackProbability {
    public static float blackjackProbability(int target, int startingHand) {
        double p = bust(target, startingHand, new HashMap<>());
        return Math.round(p * 1000) / 1000f;
    }

    private static double bust(int target, int hand, Map<Integer, Double> memo) {
        if (hand > target) return 1;
        if (hand + 4 >= target) return 0;
        Double m = memo.get(hand);
        if (m != null) return m;
        double p = 0;
        for (int c = 1; c <= 10; c++) p += 0.1 * bust(target, hand + c, memo);
        memo.put(hand, p);
        return p;
    }
}
