import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[] num_list) {
        int num1 = Integer.parseInt(IntStream.of(num_list)
            .filter(num -> num % 2 == 1)
            .mapToObj(String::valueOf)
            .collect(Collectors.joining()));
        
        int num2 = Integer.parseInt(IntStream.of(num_list)
            .filter(num -> num % 2 == 0)
            .mapToObj(String::valueOf)
            .collect(Collectors.joining()));

        return num1 + num2;
    }
}