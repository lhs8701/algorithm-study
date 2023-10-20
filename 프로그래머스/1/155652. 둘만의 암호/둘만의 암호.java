import java.util.*;
import java.util.stream.*;
class Solution {
    public String solution(String s, String skip, int index) {
        String alpha = IntStream.rangeClosed('a', 'z')
            .mapToObj(num -> String.valueOf((char)num))
            .filter(str -> !skip.contains(str))
            .collect(Collectors.joining()).repeat(3);
        return Arrays.stream(s.split(""))
            .map(str -> String.valueOf(alpha.charAt(alpha.indexOf(str) + index)))
            .collect(Collectors.joining());
    }
}