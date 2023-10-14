import java.util.*;
import java.util.stream.*;
class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        Map<Integer, Integer> map = Map.of(6,1, 5,2, 4,3, 3,4, 2,5, 1,6, 0,6);
        List<Integer> lottoList = IntStream.of(lottos)
            .boxed()
            .collect(Collectors.toList());
        Set<Integer> winSet = IntStream.of(win_nums)
            .boxed()
            .collect(Collectors.toSet());
        int numZero = Collections.frequency(lottoList, 0);
        Set<Integer> lottoSet = new HashSet<>(lottoList);
        lottoSet.retainAll(winSet);
        int numEquals = lottoSet.size();
        System.out.println(numZero + " " + numEquals);
        return new int[]{map.get(numEquals + numZero), map.get(numEquals)};
    }
}