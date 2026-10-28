public class ShortenPath {
    public static String shortenPath(String path) {
        boolean abs = path.startsWith("/");
        ArrayDeque<String> st = new ArrayDeque<>();
        for (String t : path.split("/")) {
            if (t.isEmpty() || t.equals(".")) continue;
            if (t.equals("..")) {
                if (!st.isEmpty() && !st.peekLast().equals("..")) st.pollLast();
                else if (!abs) st.addLast("..");
            } else st.addLast(t);
        }
        String joined = String.join("/", st);
        return abs ? "/" + joined : joined;
    }
}
