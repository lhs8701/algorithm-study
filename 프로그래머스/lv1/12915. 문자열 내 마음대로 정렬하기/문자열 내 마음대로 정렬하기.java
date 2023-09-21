import java.util.*;
import java.util.stream.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        return Arrays.stream(strings)
            .sorted((a, b) -> (a.charAt(n) + "").equals(b.charAt(n) + "") ? a.compareTo(b) : (a.charAt(n) + "").compareTo((b.charAt(n) + "")))
            .toArray(String[]::new);
    }
}