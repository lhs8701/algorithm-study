import java.util.*;
import java.util.stream.*;
class Solution {
    public int[] solution(int num, int total) {
        return num % 2 == 1 ? IntStream.rangeClosed(total/num - num/2, total/num + num/2).toArray() : IntStream.rangeClosed(total/num - (num/2 - 1), total/num + num/2 ).toArray();
    }
}