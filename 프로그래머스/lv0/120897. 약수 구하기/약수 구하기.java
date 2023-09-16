import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int n) {
        int[] array = IntStream.range(1, n+1)
            .filter(num -> n % num == 0)
            .toArray();
        return array;
    }
}