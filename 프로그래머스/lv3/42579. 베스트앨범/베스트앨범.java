import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, List<Integer>> map = new HashMap<>();
        for(int i=0; i<plays.length; i++) {
            map.putIfAbsent(genres[i], new ArrayList<>());
            map.get(genres[i]).add(i);
        }
        return map.values().stream()
                .sorted((a, b) -> b.stream().mapToInt(i -> plays[i]).sum() - a.stream().mapToInt(i -> plays[i]).sum())
                .map(list -> list.stream().sorted((a, b) -> plays[a] == plays[b] ? a - b : plays[b] - plays[a]).limit(2).collect(Collectors.toList()))
                .flatMap(Collection::stream)
                .mapToInt(Integer::intValue)
                .toArray();
    }
}