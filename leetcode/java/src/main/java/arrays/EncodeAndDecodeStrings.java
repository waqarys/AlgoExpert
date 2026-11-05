package arrays;

import java.util.*;

/**
 * LC 271 Encode and Decode Strings.
 * Approach: length-prefix framing "len#word"; decoding reads the length then exactly len chars.
 * Time O(N), Space O(N) where N = total characters.
 */
public class EncodeAndDecodeStrings {
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String s : strs) sb.append(s.length()).append('#').append(s);
        return sb.toString();
    }

    public List<String> decode(String s) {
        List<String> out = new ArrayList<>();
        int i = 0;
        while (i < s.length()) {
            int j = s.indexOf('#', i);
            int len = Integer.parseInt(s.substring(i, j));
            out.add(s.substring(j + 1, j + 1 + len));
            i = j + 1 + len;
        }
        return out;
    }
}
