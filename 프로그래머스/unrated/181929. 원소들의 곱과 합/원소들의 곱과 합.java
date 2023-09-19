import java.util.stream.*;

class Solution {
    public int solution(int[] num_list) {
        return IntStream.of(num_list).reduce(1, (x, y) -> x * y) < Math.pow(IntStream.of(num_list).sum(), 2) ? 1 : 0;
    }
}