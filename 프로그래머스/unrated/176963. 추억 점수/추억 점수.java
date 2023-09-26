import java.util.*;
import java.util.stream.*;
class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        Map<String, Integer> map = new HashMap<>();
        for(int i=0; i<name.length; i++){
            map.put(name[i], yearning[i]);
        }
        return Arrays.stream(photo)
            .mapToInt(arr -> Arrays.stream(arr).mapToInt(str -> map.getOrDefault(str, 0)).sum())
            .toArray();
    }
}