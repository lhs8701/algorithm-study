import java.util.*;
import java.util.stream.*;

class Solution {
    String[] words = new String[]{"aya", "ye", "woo", "ma"};
    public int solution(String[] babbling) {
        return Arrays.stream(babbling)
            .mapToInt(bab -> func(bab))
            .sum();
    }
    
    int func(String str){
        int prev = -1;
        while (!str.isBlank()){
            boolean success = false;
            for(int i=0; i<4; i++){
                if (i == prev){
                    continue;
                }
                String word = words[i];
                if (str.substring(0, Math.min(word.length(), str.length())).equals(word)){
                    str = str.substring(word.length());
                    prev = i;
                    success = true;
                    break;
                }
            }
            if (!success){
                return 0;
            }
        }
        return 1;
    }
}