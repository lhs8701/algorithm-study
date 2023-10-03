import java.util.stream.*;
class Solution {
    public int[] solution(int[] arr, int n) {
        return IntStream.range(0, arr.length)
            .map(i -> i % 2 == arr.length % 2 ? arr[i] : arr[i] + n)
            .toArray();
    }
}