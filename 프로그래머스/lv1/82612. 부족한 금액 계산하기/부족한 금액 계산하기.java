import java.util.*;
import java.util.stream.*;
class Solution {
    public long solution(int price, int money, int count) {
        return Math.max(LongStream.iterate(price, num -> num + price)
            .limit(count)
            .sum() - money, 0);
    }
}