import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[] array) {
        return IntStream.of(array)
            .mapToObj(String::valueOf)
            .map(str -> Collections.frequency(Arrays.stream(str.split("")).collect(Collectors.toList()), "7"))
            .mapToInt(Integer::intValue)
            .sum();
    }
}