import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(long n) {
        List<String> list = Arrays.stream(String.valueOf(n).split(""))
            .collect(Collectors.toList());
        Collections.reverse(list);
        return list.stream()
            .mapToInt(Integer::parseInt)
            .toArray();
    }
}