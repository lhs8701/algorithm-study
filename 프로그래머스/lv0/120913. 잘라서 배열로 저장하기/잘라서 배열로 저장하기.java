import java.util.*;
import java.util.stream.*;

class Solution {
    public String[] solution(String my_str, int n) {
        return IntStream.iterate(0, num -> num + n)
            .limit((long) Math.ceil(my_str.length() * 1.0 / n))
            .mapToObj(num -> my_str.substring(num, Math.min(num + n, my_str.length())))
            .toArray(String[]::new);
    }
}