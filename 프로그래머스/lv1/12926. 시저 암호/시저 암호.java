import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String s, int n) {
        return s.chars()
            .mapToObj(c -> func((char)c, n))
            .collect(Collectors.joining());
    }
    
    public String func(char ch, int n){
        if (ch == ' '){
            return " ";
        }
        if (Character.isUpperCase(ch)){
            return String.valueOf((char)('A' + (ch + n - 'A') % 26));
        }
        return String.valueOf((char)('a' + (ch + n - 'a') % 26));
    }
}