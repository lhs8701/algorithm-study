import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(String[] babbling) {
        return Arrays.stream(babbling)
            .mapToInt(str -> func(str))
            .sum();
    }
    
    public int func(String str){
        String[] token = new String[]{"aya", "ye", "woo", "ma"};
        while (!str.isBlank()){
            boolean flag = false;
            for(String t : token){
                if (str.contains(t)){
                    str = str.replaceAll(t, " ");
                    flag = true;
                    break;
                }
            }
            if (!flag){
                return 0;
            }
        }
        return 1;
    }
}