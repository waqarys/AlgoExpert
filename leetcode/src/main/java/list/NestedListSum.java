package list;

import java.util.LinkedList;

public class NestedListSum {
    public int depthSum(List<NestedInteger> nestedList) {
        int sum = 0;
        int lv = 1;

        while(nestedList.size() != 0) {
            List<NestedList> tmp = new LinkedList<>();
            for(NestedList e : nestedList) {
                if(e.isInteger()) {
                    sum += e.getInteger() * lv;
                } else {
                    tmp.addAll(e.getList);
                }
            }
            lv++;
            nestedList = tmp;
        }

        return sum;
    }
}
