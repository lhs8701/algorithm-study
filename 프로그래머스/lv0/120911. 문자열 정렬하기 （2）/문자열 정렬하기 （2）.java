import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String my_string) {
        return Arrays.stream(my_string.toLowerCase().split(""))
            .sorted(Comparator.comparing(n -> n))
            .collect(Collectors.joining());
    }
}