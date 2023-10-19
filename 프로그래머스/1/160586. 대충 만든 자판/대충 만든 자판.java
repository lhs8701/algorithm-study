import java.util.*;
import java.util.stream.*;
class Solution {
    public Map<String, Integer> map;
    public int[] solution(String[] keymap, String[] targets) {
         map = IntStream.rangeClosed('A', 'Z')
                .mapToObj(num -> String.valueOf((char)num))
                .collect(Collectors.toMap(key -> key, key -> Arrays.stream(keymap)
                        .mapToInt(str -> str.indexOf(key) + 1)
                        .filter(num -> num != 0)
                        .min().orElse(0)));
        return Arrays.stream(targets)
            .mapToInt(str -> getCount(str))
            .toArray();
    }
    public int getCount(String str){
        int sum = 0;
        for (String ch : str.split("")){
            if (map.get(ch) == 0){
                return -1;
            }
            sum += map.get(ch);
        }
        return sum;
    }
}