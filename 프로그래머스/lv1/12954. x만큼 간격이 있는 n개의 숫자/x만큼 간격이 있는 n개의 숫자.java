import java.util.*;
import java.util.stream.*;

class Solution {
    public long[] solution(int x, int n) {
        return LongStream.iterate(x, num -> (long)num + x)
            .limit(n)
            .toArray();
    }
}