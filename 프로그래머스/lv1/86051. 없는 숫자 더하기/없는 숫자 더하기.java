import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[] numbers) {
        return 45 - IntStream.of(numbers).sum();
    }
}