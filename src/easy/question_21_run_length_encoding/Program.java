package easy.question_21_run_length_encoding;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in a non-empty string and returns its run-length
 *   encoding.
 * </p>
 * <p>
 *   From Wikipedia, "run-length encoding is a form of lossless data compression in
 *   which runs of data are stored as a single data value and count, rather than as
 *   the original run." For this problem, a run of data is any sequence of
 *   consecutive, identical characters. So the run <span>"AAA"</span> would be
 *   run-length-encoded as <span>"3A"</span>.
 * </p>
 * <p>
 *   To make things more complicated, however, the input string can contain all
 *   sorts of special characters, including numbers. And since encoded data must be
 *   decodable, this means that we can't naively run-length-encode long runs. For
 *   example, the run <span>"AAAAAAAAAAAA"</span> (12 <span>A</span>s), can't
 *   naively be encoded as <span>"12A"</span>, since this string can be decoded as
 *   either <span>"AAAAAAAAAAAA"</span> or <span>"1AA"</span>. Thus, long runs (runs
 *   of 10 or more characters) should be encoded in a split fashion; the
 *   aforementioned run should be encoded as <span>"9A3A"</span>.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">string</span> = "AAAAAAAAAAAAABBCCCCDD"
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>"9A4A2B4C2D"
 * </pre>
 * </div>
 */
public class Program {
    public static void main(String[] args) {
        var input = "AAAAAAAAAAAAABBCCCCDD";
        var expected = "9A4A2B4C2D";
        System.out.println(runLengthEncoding(input).equals(expected));
    }

    // O(n) time | O(n) space - where n is the length of the input string
    public static String runLengthEncoding(String string) {
        StringBuilder encodedStringCharacters = new StringBuilder();
        int currentRunLenght = 1;

        for (int i = 1; i< string.length(); i++) {
            char currentCharacter = string.charAt(i);
            char previousCharacter = string.charAt(i - 1);

            if ((currentCharacter != previousCharacter) || (currentRunLenght == 9)) {
                encodedStringCharacters.append(Integer.toString(currentRunLenght));
                encodedStringCharacters.append(previousCharacter);
                currentRunLenght = 0;
            }

            currentRunLenght += 1;
        }

        //Handle the last run
        encodedStringCharacters.append(Integer.toString(currentRunLenght));
        encodedStringCharacters.append(string.charAt(string.length() - 1));

        return encodedStringCharacters.toString();
    }
}
