import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(String s) {
        List<Integer> list = new ArrayList();
        for(int i=0, n=s.length(); i<n; i++){
            String ch = s.charAt(i) + "";
            int idx = s.substring(0, i).lastIndexOf(ch);
            list.add(idx == -1 ? -1 : i - idx);
        }
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}