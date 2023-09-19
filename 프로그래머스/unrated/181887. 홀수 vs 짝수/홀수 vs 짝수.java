import java.util.stream.*;
class Solution {
    public int solution(int[] num_list) {
        int even = IntStream.range(0, num_list.length).filter(i -> i % 2 == 0).map(i -> num_list[i]).sum();
        int odd = IntStream.range(0, num_list.length).filter(i -> i % 2 == 1).map(i -> num_list[i]).sum();
        return Math.max(even, odd);
    }
}