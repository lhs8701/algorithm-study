import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String polynomial) {
        int a = Arrays.stream(polynomial.split(" \\+ "))
            .filter(str -> str.contains("x"))
            .mapToInt(str -> str.length() == 1 ? 1 : Integer.parseInt(str.substring(0, str.indexOf("x"))))
            .sum();
        
        int b = Arrays.stream(polynomial.split(" \\+ "))
            .filter(str -> !str.contains("x"))
            .mapToInt(Integer::parseInt)
            .sum();
        
        String prefix = a == 1 ? "x" : a != 0 ? a + "x" : "";
        return b==0? prefix : (prefix.equals("") ? b + "" : prefix + " + " + b);
    }
}