package easy.question20_ceaser_cipher;

/**
 * <div class="html">
 * <p>
 *   Given a non-empty string of lowercase letters and a non-negative integer
 *   representing a key, write a function that returns a new string obtained by
 *   shifting every letter in the input string by k positions in the alphabet,
 *   where k is the key.
 * </p>
 * <p>
 *   Note that letters should "wrap" around the alphabet; in other words, the
 *   letter <span>z</span> shifted by one returns the letter <span>a</span>.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">string</span> = "xyz"
 * <span class="CodeEditor-promptParameter">key</span> = 2
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>"zab"
 * </pre>
 * </div>
 */
public class Program {
    public static void main(String[] args) {
        System.out.println(caesarCypherEncryptor("Waqar", 4));
    }

    public static String caesarCypherEncryptor(String str, int key) {
        char[] newLetters = new char[str.length()];
        int newKey = key % 26;
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        for (int i = 0; i < str.length(); i++) {
            newLetters[i] = getNewLetter(str.charAt(i), newKey, alphabet);
        }
        return new String(newLetters);
    }

    public static char getNewLetter(char letter, int key, String alphabet) {
        int newLetterCode = alphabet.indexOf(letter) + key;
        return alphabet.charAt(newLetterCode % 26);
    }
}
