import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String cipher, int code) {
        int length = cipher.length();
        String str = Stream.iterate(code, num -> num + code)
            .limit(length / code)
            .map(i  -> String.valueOf(cipher.charAt(i - 1)))
            .collect(Collectors.joining());
        String answer = str;
        return answer;
    }
}