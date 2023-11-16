import java.util.*;
import java.util.stream.*;
class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        Set<Integer> aSet = new LinkedHashSet<>(IntStream.of(arr).boxed().collect(Collectors.toList()));
        Set<Integer> dSet = new LinkedHashSet<>(IntStream.of(delete_list).boxed().collect(Collectors.toList()));
        aSet.removeAll(dSet);
        return aSet.stream().mapToInt(Integer::intValue).toArray();
    }
}