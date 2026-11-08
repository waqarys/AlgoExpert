# 0211. Design Add and Search Words Data Structure

**Difficulty:** Medium | **Category:** Tries | **LeetCode:** https://leetcode.com/problems/design-add-and-search-words-data-structure/

## Problem
- addWord(word) and search(pattern) where '.' matches any single letter.

## Intuition
- Store words in a trie. For a normal letter follow one child; for '.' try every child (DFS/backtracking).

## Brute Force
- Store a list and regex-match every word: O(N * L) per search.

## Optimal Approach
1. addWord: standard trie insert.
2. dfs(node, i): if i == len return node.end.
3. If pattern[i] == '.', return true if any child c has dfs(c, i+1). Else follow the matching child.

## Worked Example
```text
add bad, dad, mad
search "pad" -> no 'p' child -> false
search "bad" -> true
search ".ad" -> try b: a,d end -> true
search "b.." -> b -> a -> d end -> true
```

## Complexity
- add O(L). search O(L) without dots, O(26^d * L) worst case with d dots.

## Pitfalls
- A pattern longer than every word must return false, not throw.

## Video Script
- Builds directly on problem 208; the only change is branching on '.'.

## Solution
```java file=tries/WordDictionary.java
package tries;

/**
 * LC 211 Design Add and Search Words Data Structure.
 * Approach: trie; '.' explores all children via DFS.
 * add O(L), search O(26^dots * L) worst case.
 */
public class WordDictionary {
    private static class Node {
        Node[] next = new Node[26];
        boolean end;
    }

    private final Node root = new Node();

    public void addWord(String word) {
        Node n = root;
        for (char c : word.toCharArray()) {
            if (n.next[c - 'a'] == null) n.next[c - 'a'] = new Node();
            n = n.next[c - 'a'];
        }
        n.end = true;
    }

    public boolean search(String word) { return dfs(root, word, 0); }

    private boolean dfs(Node n, String w, int i) {
        if (i == w.length()) return n.end;
        char c = w.charAt(i);
        if (c == '.') {
            for (Node child : n.next) if (child != null && dfs(child, w, i + 1)) return true;
            return false;
        }
        Node child = n.next[c - 'a'];
        return child != null && dfs(child, w, i + 1);
    }
}
```

## Tests
```java test=tries/WordDictionaryTest.java
package tries;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class WordDictionaryTest {
    @Test void example() {
        WordDictionary d = new WordDictionary();
        d.addWord("bad"); d.addWord("dad"); d.addWord("mad");
        assertFalse(d.search("pad"));
        assertTrue(d.search("bad"));
        assertTrue(d.search(".ad"));
        assertTrue(d.search("b.."));
        assertFalse(d.search("b..."));
        assertFalse(d.search("."));
    }
}
```
