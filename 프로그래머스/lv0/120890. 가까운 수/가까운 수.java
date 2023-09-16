import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[] array, int n) {
        List<Integer> list = IntStream.of(array).boxed().collect(Collectors.toList());
        List<Integer> gap = list.stream()
            .map(num -> (int)Math.abs(n - num))
            .collect(Collectors.toList());
        int minGap = Collections.min(gap);
        return list.contains(n - minGap)? n - minGap : n + minGap;
    }
}