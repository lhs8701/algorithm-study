import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[][] score) {
        List<Double> original = Arrays.stream(score)
            .mapToDouble(arr -> (arr[0] + arr[1]) / 2.0)
            .boxed()
            .collect(Collectors.toList());
        original.forEach(System.out::println);
        
        List<Double> sorted = original.stream()
            .sorted(Comparator.reverseOrder())
            .distinct()
            .collect(Collectors.toList());
        List<Integer> frequency = original.stream()
            .sorted(Comparator.reverseOrder())
            .distinct()
            .map(n -> Collections.frequency(original, n))
            .collect(Collectors.toList());
        
        int start = 1;
        int[] rank = new int[frequency.size()];
        for(int i=0; i<frequency.size(); i++){
            rank[i] = start; 
            start += frequency.get(i);
        }
        
        int[] answer = new int[original.size()];
        for(int i=0, n=original.size(); i<n; i++){
            int idx = sorted.indexOf(original.get(i));
            answer[i] = rank[idx];
        }
        return answer;
    }
}