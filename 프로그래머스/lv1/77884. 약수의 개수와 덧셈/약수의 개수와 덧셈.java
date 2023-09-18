import java.util.*;
import java.util.stream.*;
class Solution {
    public int solution(int left, int right) {
        return 
            IntStream.rangeClosed(left, right)
            .map(num -> IntStream.rangeClosed(1, num).filter(n -> num % n == 0).count() % 2 == 0 ? num : -num)
            .sum();
    }
}