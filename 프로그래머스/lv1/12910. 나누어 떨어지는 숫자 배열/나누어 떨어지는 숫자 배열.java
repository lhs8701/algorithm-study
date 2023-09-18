import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] array = IntStream.of(arr)
            .filter(num -> num % divisor == 0)
            .sorted()
            .toArray();
        return array.length == 0 ? new int[]{-1} : array;
    }
}