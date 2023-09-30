import java.util.*;
class Solution {
    public int solution(int n, String control) {
        String[] arr = control.split("");
        Map<String, Integer> map = Map.of("w", +1, "s", -1, "d", +10, "a", -10);
        for(String ch : arr){
            n += map.get(ch);
        }
        return n;
    }
}