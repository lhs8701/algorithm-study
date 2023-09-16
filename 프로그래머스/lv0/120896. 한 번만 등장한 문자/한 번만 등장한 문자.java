import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String s) {
        List<String> list = Arrays.stream(s.split(""))
            .collect(Collectors.toList());
        
        return list.stream()
            .filter(str -> Collections.frequency(list, str) == 1)
            .sorted()
            .collect(Collectors.joining());
    }
}