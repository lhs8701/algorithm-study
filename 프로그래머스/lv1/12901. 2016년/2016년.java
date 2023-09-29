import java.util.stream.*;

class Solution {
    public String solution(int a, int b) {
        int[] ends = new int[]{31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        String[] weekDays = new String[]{"MON","TUE","WED","THU","FRI","SAT","SUN"};
        int sum = IntStream.range(0, a - 1)
            .map(i -> ends[i])
            .sum() + b - 1;
        return weekDays[(4 + sum) % 7];
    }
}