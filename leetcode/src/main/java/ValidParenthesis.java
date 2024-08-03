import java.util.Stack;

public class ValidParenthesis {

    public int minAddToMakeValid(String s) {
        Stack<Character> stack = new Stack<>();

        for(char c: s.toCharArray()) {
            if(c == '(') {
                stack.push(c);
            } else {
                if(!stack.isEmpty() && stack.peek() == '(') {
                    stack.pop();
                } else {
                    stack.push(c);
                }
            }
        }
        return stack.size();
    }
    public int minAddToMakeValid1(String s) {
        int left = 0;
        int right = 0;

        for(char c : s.toCharArray()) {
            if(c == '(') {
                left ++;
            } else {
                if(left > 0) {
                    left --;
                } else {
                    right ++;
                }
            }
        }
        return left + right;
    }
}
