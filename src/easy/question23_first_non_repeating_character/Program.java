package easy.question23_first_non_repeating_character;

import java.util.HashMap;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in a string of lowercase English-alphabet letters
 *   and returns the index of the string's first non-repeating character.
 * </p>
 * <p>
 *   The first non-repeating character is the first character in a string that
 *   occurs only once.
 * </p>
 * <p>
 *   If the input string doesn't have any non-repeating characters, your function
 *   should return <span>-1</span>.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">string</span> = "abcdcaf"
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>1 <span class="CodeEditor-promptComment">// The first non-repeating character is "b" and is found at index 1.</span>
 * </pre>
 * </div>
 */
public class Program {

    public static void main(String[] args) {
        String input = "abcdcaf";
        int expected = 1;
        var actual = firstNonRepeatingCharacter(input);
        System.out.println(actual == expected);
    }

    public static int firstNonRepeatingCharacter(String string) {
        HashMap<Character, Integer> characterFrequencies = new HashMap<Character, Integer>();

        for(int idx = 0; idx < string.length(); idx++) {
            char character = string.charAt(idx);
            characterFrequencies.put(character, characterFrequencies.getOrDefault(character, 0) + 1);
        }

        for(int idx = 0; idx < string.length(); idx++) {
            char character = string.charAt(idx);
            if(characterFrequencies.get(character) == 1){
                return idx;
            }
        }

        return -1;
    }
}
