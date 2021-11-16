package easy.question19_palindrome;

public class Program3 {
    public static void main(String[] args) {
        System.out.println(isPalindrome("abcdcba"));
    }

    public static boolean isPalindrome(String str) {
        int leftIdx = 0;
        int rightIdx = str.length() -1;
        while (leftIdx < rightIdx) {
            if (str.charAt(leftIdx) !=  str.charAt(rightIdx)) {
                return false;
            }
            leftIdx++;
            rightIdx--;
        }
        return true;
    }
}
