import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String s) {
        return Arrays.stream(s.split(""))
            .sorted((a, b) -> b.compareTo(a))
            .collect(Collectors.joining());
    }
}