import java.util.*;
import java.util.stream.*;

class Solution {
    public boolean solution(int x) {
        return x % (Arrays.stream(String.valueOf(x).split(""))
            .mapToInt(Integer::parseInt)
            .sum()) == 0;
    }
}