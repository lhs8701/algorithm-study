import java.util.*;
import java.util.stream.*;
class Solution {
    public int solution(String before, String after) {
        String str1 = Arrays.stream(before.split(""))
            .sorted()
            .collect(Collectors.joining());
        
        String str2 = Arrays.stream(after.split(""))
            .sorted()
            .collect(Collectors.joining());
        
        return (str1.equals(str2))? 1 : 0;
    }
}