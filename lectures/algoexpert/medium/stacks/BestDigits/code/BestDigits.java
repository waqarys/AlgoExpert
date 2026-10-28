public class BestDigits {
    public static String bestDigits(String number, int numDigits) {
        ArrayDeque<Character> st = new ArrayDeque<>();
        int k = numDigits;
        for (char c : number.toCharArray()) {
            while (k > 0 && !st.isEmpty() && st.peekLast() < c) { st.pollLast(); k--; }
            st.addLast(c);
        }
        while (k-- > 0) st.pollLast();
        StringBuilder sb = new StringBuilder();
        for (char c : st) sb.append(c);
        return sb.toString();
    }
}
