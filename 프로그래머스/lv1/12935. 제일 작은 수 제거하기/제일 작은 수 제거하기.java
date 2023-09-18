import java.util.*;
import java.util.stream.*;
class Solution {
    public int[] solution(int[] arr) {
        int m = IntStream.of(arr).min().getAsInt();
        int[] answer =  IntStream.of(arr).filter(num -> num != m).toArray();
        return answer.length == 0 ? new int[]{-1} : answer;
    }
}