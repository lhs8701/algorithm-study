import java.util.*;
import java.util.stream.*;
class Solution {
    public int[] solution(int[] num_list) {
        int first = num_list[num_list.length-1];
        int second = num_list[num_list.length-2];
        List<Integer> list = IntStream.of(num_list)
            .boxed()
            .collect(Collectors.toList());
        List<Integer> answer = new ArrayList<>();
        answer.addAll(list);
        answer.add(first > second ? first - second : first * 2);
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}