public class StringsMadeUpOfStrings {
    public static String[] stringsMadeUpOfStrings(String[] strings, String[] substrings) {
        Set<String> dict = new HashSet<>(Arrays.asList(substrings));
        List<String> out = new ArrayList<>();
        for (String s : strings) {
            int n = s.length();
            int[] pieces = new int[n + 1];
            Arrays.fill(pieces, -1);
            pieces[0] = 0;
            for (int j = 1; j <= n; j++)
                for (int i = 0; i < j; i++)
                    if (pieces[i] >= 0 && dict.contains(s.substring(i, j))) pieces[j] = Math.max(pieces[j], pieces[i] + 1);
            if (pieces[n] >= 2) out.add(s);
        }
        return out.toArray(new String[0]);
    }
}
