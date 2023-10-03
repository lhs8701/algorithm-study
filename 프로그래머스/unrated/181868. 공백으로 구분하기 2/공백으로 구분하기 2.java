import java.util.*;
import java.util.stream.*;
class Solution {
    public String[] solution(String my_string) {
        return Arrays.stream(my_string.split(" ")).filter(str -> str.length() != 0).toArray(String[]::new);
    }
}