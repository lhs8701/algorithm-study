import java.util.stream.*;

class Solution {
    public int[] solution(int[] num_list, int n) {
        return IntStream.iterate(0, i -> i + n)
            .limit((int)Math.ceil(num_list.length*1.0/n))
            .map(i -> num_list[i])
            .toArray();
    }
}