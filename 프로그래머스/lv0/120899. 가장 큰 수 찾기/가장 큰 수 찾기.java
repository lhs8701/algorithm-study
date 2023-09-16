import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] array) {
        List<Integer> list = Arrays.stream(array)
            .boxed()
            .collect(Collectors.toList());
        int val = list.stream().max(Integer::compareTo).orElse(0);
        return new int[]{val, list.indexOf(val)};
    }
}