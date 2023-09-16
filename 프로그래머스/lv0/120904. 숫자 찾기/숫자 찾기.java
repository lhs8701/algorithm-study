import java.util.*;

class Solution {
    public int solution(int num, int k) {
        int ans = String.valueOf(num).indexOf(String.valueOf(k));
        return (ans == -1) ? -1 : ans + 1;
    }
}