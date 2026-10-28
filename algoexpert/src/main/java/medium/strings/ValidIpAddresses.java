package medium.strings;

import java.util.ArrayList;
import java.util.List;

/**
 * Valid IP Addresses: all ways to insert three dots into a digit string to form valid IPv4 addresses
 * (each part 0-255, no leading zeros).
 * Time: O(1) (bounded by 3^3 splits) | Space: O(1).
 */
public class ValidIpAddresses {
    public static ArrayList<String> validIPAddresses(String s) {
        ArrayList<String> out = new ArrayList<>();
        for (int i = 1; i < Math.min(4, s.length()); i++)
            for (int j = i + 1; j < Math.min(i + 4, s.length()); j++)
                for (int k = j + 1; k < Math.min(j + 4, s.length()); k++) {
                    String[] p = {s.substring(0, i), s.substring(i, j), s.substring(j, k), s.substring(k)};
                    if (valid(p[0]) && valid(p[1]) && valid(p[2]) && valid(p[3])) out.add(String.join(".", p));
                }
        return out;
    }

    private static boolean valid(String p) {
        if (p.isEmpty() || p.length() > 3 || (p.length() > 1 && p.charAt(0) == '0')) return false;
        return Integer.parseInt(p) <= 255;
    }
}
