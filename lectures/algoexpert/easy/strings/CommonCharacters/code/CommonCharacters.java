public class CommonCharacters {
    public static String[] commonCharacters(String[] strings) {
        Set<Character> common = null;
        for (String s : strings) {
            Set<Character> cur = new HashSet<>();
            for (char c : s.toCharArray()) cur.add(c);
            if (common == null) common = cur; else common.retainAll(cur);
        }
        List<String> out = new ArrayList<>();
        for (char c : new TreeSet<>(common)) out.add(String.valueOf(c));
        return out.toArray(new String[0]);
    }
}
