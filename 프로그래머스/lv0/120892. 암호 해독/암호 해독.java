import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String cipher, int code) {
        return Stream.iterate(code, num -> num + code)
            .limit(cipher.length() / code)
            .map(i  -> String.valueOf(cipher.charAt(i - 1)))
            .collect(Collectors.joining());
    }
}