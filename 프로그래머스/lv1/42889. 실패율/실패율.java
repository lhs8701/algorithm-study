import java.util.*;
import java.util.stream.*;
import java.util.stream.Collectors.*;
class Solution {
    public int[] solution(int N, int[] stages) {
        Map<Integer, Long> map = IntStream.of(stages)
            .boxed()
            .collect(Collectors.groupingBy(n -> n, Collectors.counting()));
        int remain = stages.length;
        double[] order = new double[N+1];
        for(int i=1; i<=N ;i++){
            int ongoing = map.getOrDefault(i, 0L).intValue();
            order[i] = (double)ongoing / Math.max(1, remain);
            remain -= ongoing;
        }
        DoubleStream.of(order)
            .forEach(System.out::println);
        return IntStream.rangeClosed(1, N)
            .boxed()
            .sorted((a, b) -> order[a] == order[b] ? Integer.compare(a, b) : Double.compare(order[b], order[a]))
            .mapToInt(Integer::intValue)
            .toArray();
    }
}