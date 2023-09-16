import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(String[] spell, String[] dic) {
        String key = Arrays.stream(spell)
            .sorted()
            .collect(Collectors.joining(""));
        
         return (Arrays.stream(dic)
            .map(s -> Arrays.stream(s.split("")).sorted().collect(Collectors.joining()))
            .filter(s -> s.equals(key))
            .findFirst()
            .isEmpty()) ? 2 : 1;
    }
}