import java.util.*;
import java.util.stream.*;

class Solution {
    public long solution(long n) {
        long x = LongStream.rangeClosed(1, (long)Math.sqrt(n))
            .filter(num -> num * num == n)
            .findFirst().orElse(-1);
        return x == -1 ? -1 : (x+1) * (x+1);
    }
}