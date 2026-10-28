public class PhoneNumberMnemonics {
    private static final String[] KEYS = {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public static List<String> phoneNumberMnemonics(String phone) {
        List<String> out = new ArrayList<>();
        build(phone, 0, new StringBuilder(), out);
        return out;
    }

    private static void build(String p, int i, StringBuilder sb, List<String> out) {
        if (i == p.length()) { out.add(sb.toString()); return; }
        for (char c : KEYS[p.charAt(i) - '0'].toCharArray()) { sb.append(c); build(p, i + 1, sb, out); sb.setLength(sb.length() - 1); }
    }
}
