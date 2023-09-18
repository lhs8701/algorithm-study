import java.util.*;
import java.util.stream.*;

class Solution {
    public long solution(long n) {
        String str = Arrays.stream(String.valueOf(n).split(""))
            .map(Integer::parseInt)
            .sorted((a, b) -> b - a)
            .map(String::valueOf)
            .collect(Collectors.joining());
        return Long.parseLong(str);
    }
}