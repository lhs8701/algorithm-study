import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        Set<Integer> commons = IntStream.of(lost).boxed().collect(Collectors.toSet());
        commons.retainAll(IntStream.of(reserve).boxed().collect(Collectors.toSet()));
        int count = 0;
        boolean[] arr = new boolean[n+1];
        Arrays.fill(arr, false);
        for(int num : reserve){
            if (commons.contains(num)){
                continue;
            }
            arr[num] = true;
        }
        Arrays.sort(lost);
        for(int num : lost){
            if (commons.contains(num)){
                continue;
            }
            if (1 < num && arr[num-1]){
                arr[num-1] = false;
                count++;
            }
            else if (num < n && arr[num+1]){
                arr[num+1] = false;
                count++;
            }
        }
        int answer = n - lost.length + commons.size() + count;
        return answer;
    }
}