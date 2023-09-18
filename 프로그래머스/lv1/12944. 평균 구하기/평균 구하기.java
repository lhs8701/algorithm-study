import java.util.stream.*;
class Solution {
    public double solution(int[] arr) {
        return IntStream.of(arr)
            .average().getAsDouble();
    }
}