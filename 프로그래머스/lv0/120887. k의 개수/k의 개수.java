import java.util.*;
import java.util.stream.*;
class Solution {
    public int solution(int i, int j, int k) {
        return (int) IntStream.rangeClosed(i, j)
            .mapToLong(num -> String.valueOf(num).chars().filter(n -> n == k + '0').count())
            .sum();
    }
}