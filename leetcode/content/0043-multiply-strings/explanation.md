# 0043. Multiply Strings

**Difficulty:** Medium | **Category:** Math & Geometry | **LeetCode:** https://leetcode.com/problems/multiply-strings/

## Problem
- Multiply two non-negative integers given as strings, without converting them to big integers.

## Intuition
- Grade-school multiplication: digit i of num1 times digit j of num2 contributes to positions i + j and i + j + 1 of a result of length m + n.

## Brute Force
- Repeated addition: hopelessly slow.

## Optimal Approach
1. res = int[m + n].
2. For i from m-1 down and j from n-1 down: sum = d1 * d2 + res[i+j+1]; res[i+j+1] = sum % 10; res[i+j] += sum / 10.
3. Skip leading zeros when building the string.

## Worked Example
- "123" x "45".
```text
partial products placed by i+j:
3*5=15  3*4=12  2*5=10  2*4=8  1*5=5  1*4=4
res digits = 0 5 5 3 5
answer "5535"
```

## Complexity
- Time: O(m * n). Space: O(m + n).

## Pitfalls
- If either input is "0", return "0", not an empty string.

## Video Script
- Show the paper method and map each partial product to its index.

## Solution
```java file=math/MultiplyStrings.java
package math;

/**
 * LC 43 Multiply Strings.
 * Approach: grade-school multiplication into an int[m+n] with carries.
 * Time O(mn), Space O(m+n).
 */
public class MultiplyStrings {
    public String multiply(String a, String b) {
        int m = a.length(), n = b.length();
        int[] res = new int[m + n];
        for (int i = m - 1; i >= 0; i--)
            for (int j = n - 1; j >= 0; j--) {
                int sum = (a.charAt(i) - '0') * (b.charAt(j) - '0') + res[i + j + 1];
                res[i + j + 1] = sum % 10;
                res[i + j] += sum / 10;
            }
        StringBuilder sb = new StringBuilder();
        for (int d : res) if (!(sb.length() == 0 && d == 0)) sb.append(d);
        return sb.length() == 0 ? "0" : sb.toString();
    }
}
```

## Tests
```java test=math/MultiplyStringsTest.java
package math;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MultiplyStringsTest {
    MultiplyStrings s = new MultiplyStrings();
    @Test void examples() {
        assertEquals("6", s.multiply("2", "3"));
        assertEquals("56088", s.multiply("123", "456"));
        assertEquals("5535", s.multiply("123", "45"));
        assertEquals("0", s.multiply("0", "999"));
        assertEquals("998001", s.multiply("999", "999"));
    }
}
```
