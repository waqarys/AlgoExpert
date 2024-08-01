package easy.question19_palindrome;

public class Program2 {
    public static void main(String[] args) {
        System.out.println(isPalindrome("abcdcba"));
    }

    public static boolean isPalindrome(String str) {
        return isPalindrome(str, 0);
    }

    public static boolean isPalindrome(String str, int i) {
        int j = str.length() - 1 -1;
        return i >= j ? true : str.charAt(i) == str.charAt(j) && isPalindrome(str, i + 1);
    }
}
