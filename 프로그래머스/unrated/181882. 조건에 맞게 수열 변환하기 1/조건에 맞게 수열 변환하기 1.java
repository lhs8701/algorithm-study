import java.util.stream.*;
class Solution {
    public int[] solution(int[] arr) {
        return IntStream.of(arr)
            .map(num -> num >=50 && num % 2 == 0 ? num / 2 : num < 50 && num % 2 == 1 ? num * 2 : num)
            .toArray();
    }
}