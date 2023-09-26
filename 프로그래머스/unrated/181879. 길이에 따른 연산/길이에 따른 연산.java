import java.util.stream.*;

class Solution {
    public int solution(int[] num_list) {
        return num_list.length >= 11 ? IntStream.of(num_list).sum() : IntStream.of(num_list).reduce(1, (a, b) -> a * b);
    }
}