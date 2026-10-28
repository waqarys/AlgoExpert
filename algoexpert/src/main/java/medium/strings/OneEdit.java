package medium.strings;

/**
 * One Edit: are two strings at most one insert/delete/replace apart?
 * Time: O(n) | Space: O(1).
 */
public class OneEdit {
    public static boolean oneEdit(String a, String b) {
        if (Math.abs(a.length() - b.length()) > 1) return false;
        int i = 0, j = 0;
        boolean edited = false;
        while (i < a.length() && j < b.length()) {
            if (a.charAt(i) != b.charAt(j)) {
                if (edited) return false;
                edited = true;
                if (a.length() > b.length()) i++;
                else if (a.length() < b.length()) j++;
                else { i++; j++; }
            } else { i++; j++; }
        }
        return true;
    }
}
