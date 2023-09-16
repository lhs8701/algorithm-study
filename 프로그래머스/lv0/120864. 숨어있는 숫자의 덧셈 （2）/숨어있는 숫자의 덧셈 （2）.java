import java.util.*;
import java.util.stream.*;
import java.util.function.*;

class Solution {
    public int solution(String my_string) {
        return Arrays.stream(my_string.split("[a-z]|[A-Z]"))
            .filter(Predicate.not(String::isBlank))
            .mapToInt(Integer::parseInt)
            .sum();
    }
}