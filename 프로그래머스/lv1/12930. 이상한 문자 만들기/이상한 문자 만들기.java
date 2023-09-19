import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        
        String[] chars = s.split("");
        int n = s.length();
        int i = 0;
        while (i < n) {
            if (chars[i].equals(" ")){
                sb.append(" ");
                i++;
            }else{
                int j = i; 
                while (j < n && !chars[j].equals(" ")){
                    if ((j - i) % 2 == 0) {
                        sb.append(chars[j].toUpperCase());
                    }else{
                        sb.append(chars[j].toLowerCase());
                    }
                    j += 1;
                }
                i = j;
            }
        }
        return sb.toString();
    }
}