import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int n) {
        int[] array = IntStream.range(1, 10000)
            .filter(num -> num % 3 != 0 && !String.valueOf(num).contains("3"))
            .toArray();
        return array[n-1];
    }
}