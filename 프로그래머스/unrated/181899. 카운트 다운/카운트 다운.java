import java.util.stream.*;
class Solution {
    public int[] solution(int start, int end_num) {
        return IntStream.rangeClosed(-start, -end_num)
            .map(num -> num * -1)
            .toArray();
    }
}