public class LevenshteinDistance {
    public static int levenshteinDistance(String a, String b) {
        if (a.length() < b.length()) { String t = a; a = b; b = t; }
        int[] prev = new int[b.length() + 1], cur = new int[b.length() + 1];
        for (int j = 0; j <= b.length(); j++) prev[j] = j;
        for (int i = 1; i <= a.length(); i++) {
            cur[0] = i;
            for (int j = 1; j <= b.length(); j++)
                cur[j] = a.charAt(i - 1) == b.charAt(j - 1) ? prev[j - 1]
                        : 1 + Math.min(prev[j - 1], Math.min(prev[j], cur[j - 1]));
            int[] t = prev; prev = cur; cur = t;
        }
        return prev[b.length()];
    }
}
