import java.util.stream.*;

class Solution {
    public int[] solution(int[] num_list, int n) {
        return IntStream.range(0, n)
            .map(i -> num_list[i])
            .toArray();
    }
}