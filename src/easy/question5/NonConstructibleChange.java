package easy.question5;

import java.util.Arrays;

public class NonConstructibleChange {

    public static void main(String[] args) {
        int[] input = new int[] {5, 7, 1, 1, 2, 3, 22};
        int expected = 20;
        var actual = new NonConstructibleChange().nonConstructibleChange(input);
        System.out.println(expected == actual);
    }

    public int nonConstructibleChange(int[] coins) {
        Arrays.sort(coins);

        int currentChangeCreated = 0;
        for(int coin: coins) {
            if(coin > currentChangeCreated + 1){
                return currentChangeCreated + 1;
            }

            currentChangeCreated += coin;
        }
        return currentChangeCreated + 1;
    }
}
