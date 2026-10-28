package medium.famousalgorithms;

/**
 * Stable Internships: n interns and n teams each rank the other side; produce a stable matching
 * (Gale-Shapley with interns proposing). Returns pairs [intern, team].
 * Time: O(n^2) | Space: O(n^2).
 */
public class StableInternships {
    public static int[][] stableInternships(int[][] interns, int[][] teams) {
        int n = interns.length;
        int[][] teamRank = new int[n][n];
        for (int t = 0; t < n; t++) for (int r = 0; r < n; r++) teamRank[t][teams[t][r]] = r;
        int[] teamMatch = new int[n], next = new int[n];
        java.util.Arrays.fill(teamMatch, -1);
        java.util.ArrayDeque<Integer> free = new java.util.ArrayDeque<>();
        for (int i = 0; i < n; i++) free.add(i);
        while (!free.isEmpty()) {
            int i = free.poll(), t = interns[i][next[i]++];
            int cur = teamMatch[t];
            if (cur == -1) teamMatch[t] = i;
            else if (teamRank[t][i] < teamRank[t][cur]) { teamMatch[t] = i; free.add(cur); }
            else free.add(i);
        }
        int[][] out = new int[n][];
        for (int t = 0; t < n; t++) out[teamMatch[t]] = new int[]{teamMatch[t], t};
        return out;
    }
}
