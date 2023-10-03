import java.util.stream.*;
class Solution {
    public int solution(int[] num_list, int n) {
        return IntStream.of(num_list).anyMatch(num -> num == n) ? 1 : 0;
    }
}