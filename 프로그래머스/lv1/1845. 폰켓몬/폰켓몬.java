import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[] nums) {
        Set<Integer> set = IntStream.of(nums)
            .boxed()
            .collect(Collectors.toSet());
        return Math.min(set.size(), nums.length/2);
    }
}