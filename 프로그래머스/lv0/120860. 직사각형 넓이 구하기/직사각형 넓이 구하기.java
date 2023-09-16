import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[][] dots) {
        List<List<Integer>> list = List.of(new ArrayList<>(), new ArrayList<>());
        for (int i=0; i<2; i++){
            for(int j=0; j<4; j++){
                list.get(i).add(dots[j][i]);
            }
        }
        List<Integer> list1 = list.get(0).stream().distinct().collect(Collectors.toList());
        List<Integer> list2 = list.get(1).stream().distinct().collect(Collectors.toList());
        return Math.abs((list1.get(0) - list1.get(1)) * (list2.get(0) - list2.get(1)));
    }
}