import java.util.*;
import java.util.stream.*;

public class Solution {
    public int[] solution(int[] arr) {
        List<Integer> list = IntStream.range(1, arr.length)
            .filter(i -> arr[i-1] != arr[i])
            .map(i -> arr[i])
            .boxed()
            .collect(Collectors.toList());
        list.add(0, arr[0]);
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}