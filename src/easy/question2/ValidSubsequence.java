package easy.question2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ValidSubsequence {
    public static void main(String[] args) {
        System.out.println(isValidSubsequence(
                new ArrayList<>(Arrays.asList(5, 1, 22, 25, 6, -1, 8, 10)),
                new ArrayList<>(Arrays.asList(1, 6, -1, 10))
        ));
    }

    public static boolean isValidSubsequence(List<Integer> array, List<Integer> sequence) {
        int arrIdx = 0;
        int seqIdx = 0;
        while(arrIdx < array.size() && seqIdx < sequence.size()){
            if(array.get(arrIdx).equals(sequence.get(seqIdx))){
                seqIdx++;
            }
            arrIdx++;
        }
        return seqIdx == sequence.size();
    }

    public static boolean isValidSubsequence1(List<Integer> array, List<Integer> sequence) {
        int seqIdx = 0;
        for(var value: array){
            if(seqIdx == sequence.size()){
                break;
            }
            if(sequence.get(seqIdx).equals(value)){
                seqIdx++;
            }
        }
        return seqIdx == sequence.size();
    }
}
