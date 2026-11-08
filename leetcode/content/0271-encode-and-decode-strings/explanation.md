# 0271. Encode and Decode Strings

**Difficulty:** Medium | **Category:** Arrays & Hashing | **LeetCode:** https://leetcode.com/problems/encode-and-decode-strings/

## Problem
- Design encode(List<String>) -> String and decode(String) -> List<String> so that decode(encode(x)) == x.
- Strings may contain any character, including delimiters you might want to use.

## Intuition
- A plain delimiter fails because the delimiter can appear inside a word.
- Length-prefixing solves it: write "length#word". While decoding, read digits up to '#', then take exactly that many characters, whatever they are.

## Brute Force
- Join with a rare character or escape delimiters. Escaping works but is fiddly and error-prone.

## Optimal Approach
1. Encode: for each s append s.length(), '#', s.
2. Decode with pointer i: find j = first '#' at or after i; len = parse(i..j); word = substring(j+1, j+1+len); i = j+1+len.

## Worked Example
- Input ["lint", "co#de", ""].
```text
encode -> "4#lint5#co#de0#"
decode i=0  read "4"  -> "lint"   i=6
       i=6  read "5"  -> "co#de"  i=13
       i=13 read "0"  -> ""       i=15 end
```

## Complexity
- Time: O(total characters) for both directions.
- Space: O(total characters) for the output.

## Pitfalls
- Searching '#' from the start of the string instead of from i.
- Empty strings and an empty list must both round-trip (encode([]) = "").

## Video Script
- Show why "," as a delimiter fails with a word containing ",".
- Introduce length prefixing (same idea as HTTP Content-Length / network framing).

## Solution
```java file=arrays/EncodeAndDecodeStrings.java
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
```

## Tests
```java test=arrays/EncodeAndDecodeStringsTest.java
package arrays;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class EncodeAndDecodeStringsTest {
    EncodeAndDecodeStrings c = new EncodeAndDecodeStrings();
    @Test void roundTrip() {
        List<String> in = List.of("lint", "co#de", "", "12#ab", "😀");
        assertEquals("4#lint5#co#de0#", c.encode(List.of("lint", "co#de", "")));
        assertEquals(in, c.decode(c.encode(in)));
    }
    @Test void empty() {
        assertEquals(List.of(), c.decode(c.encode(List.of())));
        assertEquals(List.of(""), c.decode(c.encode(List.of(""))));
    }
}
```
