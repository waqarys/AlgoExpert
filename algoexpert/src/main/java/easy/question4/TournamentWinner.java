package easy.question4;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class TournamentWinner {

    public static void main(String[] args) {
        ArrayList<ArrayList<String>> competitions = new ArrayList<ArrayList<String>>();
        ArrayList<String> competition1 = new ArrayList<String>(Arrays.asList("HTML", "C#"));
        ArrayList<String> competition2 = new ArrayList<String>(Arrays.asList("C#", "Python"));
        ArrayList<String> competition3 = new ArrayList<String>(Arrays.asList("Python", "HTML"));
        competitions.add(competition1);
        competitions.add(competition2);
        competitions.add(competition3);
        ArrayList<Integer> results = new ArrayList<Integer>(Arrays.asList(0, 0, 1));
        String expected = "Python";
        var actual = new TournamentWinner().tournamentWinner(competitions, results);
        System.out.println("Expected: " + expected);
        System.out.println("Actual: " + actual);
    }
    public int HOME_TEAM_WON = 1;
    public String tournamentWinner(
            ArrayList<ArrayList<String>> competitions, ArrayList<Integer> results) {
        String currentBestTeam = "";
        HashMap<String, Integer> scores = new HashMap<String, Integer>();
        scores.put(currentBestTeam, 0);

        for(int idx = 0; idx < competitions.size(); idx++) {
            ArrayList<String> competition = competitions.get(idx);
            int result = results.get(idx);

            String homeTeam = competition.get(0);
            String awayTeam = competition.get(1);

            String winningTeam = (result == HOME_TEAM_WON) ? homeTeam : awayTeam;

            updateScores(winningTeam, 3, scores);

            if(scores.get(winningTeam) > scores.get(currentBestTeam)){
                currentBestTeam = winningTeam;
            }
        }
        return currentBestTeam;
    }

    public void updateScores(String team, int points, HashMap<String, Integer> scores) {
        if(!scores.containsKey(team)){
            scores.put(team, 0);
        }

        scores.put(team, scores.get(team) + points);
    }
}
