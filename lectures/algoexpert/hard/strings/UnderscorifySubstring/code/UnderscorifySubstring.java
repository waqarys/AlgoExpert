public class UnderscorifySubstring {
    public static String underscorifySubstring(String str, String sub) {
        boolean[] mark = new boolean[str.length()];
        for (int i = str.indexOf(sub); i != -1; i = str.indexOf(sub, i + 1))
            for (int j = i; j < i + sub.length(); j++) mark[j] = true;
        StringBuilder sb = new StringBuilder();
        // adjacent occurrences (end of one == start of next) also merge, which marking handles naturally
        for (int i = 0; i < str.length(); i++) {
            if (mark[i] && (i == 0 || !mark[i - 1])) sb.append('_');
            sb.append(str.charAt(i));
            if (mark[i] && (i == str.length() - 1 || !mark[i + 1])) sb.append('_');
        }
        return sb.toString();
    }
}
