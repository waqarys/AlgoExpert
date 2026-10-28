package easy.arrays;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Tournament Winner: competitions are [home, away] pairs, results[i]==1 means home won.
 * A win is worth 3 points; return the team with most points (guaranteed unique).
 * Time: O(n) | Space: O(k) teams.
 */
public class TournamentWinner {
    public static String tournamentWinner(List<List<String>> competitions, List<Integer> results) {
        Map<String, Integer> score = new HashMap<>();
        String best = "";
        score.put(best, 0);
        for (int i = 0; i < competitions.size(); i++) {
            String winner = results.get(i) == 1 ? competitions.get(i).get(0) : competitions.get(i).get(1);
            int s = score.merge(winner, 3, Integer::sum);
            if (s > score.get(best)) best = winner;
        }
        return best;
    }
}
