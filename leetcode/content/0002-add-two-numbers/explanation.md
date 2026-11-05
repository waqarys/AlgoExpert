# 0002. Add Two Numbers

**Difficulty:** Medium | **Category:** Linked List | **LeetCode:** https://leetcode.com/problems/add-two-numbers/

## Problem
- Two non-negative numbers are stored as reversed digit lists. Return their sum as a list in the same format.
- Example: 2->4->3 (342) + 5->6->4 (465) = 7->0->8 (807).

## Intuition
- Reversed order means the head is the ones digit, exactly the order of grade-school addition.
- Add digit by digit with a carry, and continue while either list or the carry remains.

## Brute Force
- Convert to integers and add: overflows for long lists (up to 100 digits).

## Optimal Approach
1. dummy, carry = 0.
2. While a or b or carry: sum = carry + a.val? + b.val?; append sum % 10; carry = sum / 10.

## Worked Example
- 9->9 + 1.
```text
9+1+0 = 10 -> digit 0 carry 1
9+0+1 = 10 -> digit 0 carry 1
carry 1    -> digit 1
result 0->0->1 (99 + 1 = 100)
```

## Complexity
- Time: O(max(m, n)). Space: O(max(m, n)) for the output.

## Pitfalls
- The final carry creates an extra node.

## Video Script
- "This is just column addition" - show the paper version next to the list.

## Solution
```java file=linkedlist/AddTwoNumbers.java
package linkedlist;

import common.ListNode;

/**
 * LC 2 Add Two Numbers.
 * Approach: digit-by-digit addition with carry, continuing while any input or carry remains.
 * Time O(max(m,n)), Space O(max(m,n)).
 */
public class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode a, ListNode b) {
        ListNode dummy = new ListNode(0), tail = dummy;
        int carry = 0;
        while (a != null || b != null || carry != 0) {
            int sum = carry;
            if (a != null) { sum += a.val; a = a.next; }
            if (b != null) { sum += b.val; b = b.next; }
            tail.next = new ListNode(sum % 10);
            tail = tail.next;
            carry = sum / 10;
        }
        return dummy.next;
    }
}
```

## Tests
```java test=linkedlist/AddTwoNumbersTest.java
package linkedlist;

import common.ListNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AddTwoNumbersTest {
    AddTwoNumbers s = new AddTwoNumbers();
    @Test void examples() {
        assertArrayEquals(new int[]{7, 0, 8}, ListNode.toArray(s.addTwoNumbers(ListNode.of(2, 4, 3), ListNode.of(5, 6, 4))));
        assertArrayEquals(new int[]{0}, ListNode.toArray(s.addTwoNumbers(ListNode.of(0), ListNode.of(0))));
        assertArrayEquals(new int[]{8, 9, 9, 9, 0, 0, 0, 1},
                ListNode.toArray(s.addTwoNumbers(ListNode.of(9, 9, 9, 9, 9, 9, 9), ListNode.of(9, 9, 9, 9))));
    }
}
```
