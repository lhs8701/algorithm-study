import java.util.stream.*;
class Solution {
    public int[] solution(int[] num_list, int n) {
        return IntStream.range(n-1, num_list.length)
            .map(i -> num_list[i])
            .toArray();
    }
}