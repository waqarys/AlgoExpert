package array;

import java.util.HashMap;
import java.util.Map;

public class ContainsDuplicate {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> countMap = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            if(countMap.containsKey(nums[i])) {
                return true;
            }
            countMap.put(nums[i], 1);
        }
        return false;
    }
}
