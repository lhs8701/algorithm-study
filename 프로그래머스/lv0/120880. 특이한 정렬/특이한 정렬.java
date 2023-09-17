import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] numlist, int n) {
        int[] array = IntStream.of(numlist)
            .mapToDouble(num -> Math.abs(num - n) + ((num > n) ? -0.1 : 0))
            .sorted()
            .mapToInt(num -> num == (int) num ?(int) (n - num) : (int)(num + n + 0.1))
            .toArray();
        return array;
    }
}