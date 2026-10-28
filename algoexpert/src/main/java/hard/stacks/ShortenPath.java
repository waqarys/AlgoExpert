package hard.stacks;

import java.util.ArrayDeque;
import java.util.Iterator;

/**
 * Shorten Path: simplify a Unix path (absolute or relative), resolving "." and ".." and duplicate slashes.
 * Leading ".." are kept for relative paths and dropped at the root of absolute paths.
 * Time: O(n) | Space: O(n).
 */
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
