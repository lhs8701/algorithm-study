import java.util.*;

class Solution {
    public String solution(String rsp) {
        System.out.println();
        
        Map map = Map.of('2', "0", '0', "5", '5',"2");
        System.out.println(map);   

        int length = rsp.length();
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<length; i++){
            char token = rsp.charAt(i);
            sb.append(map.get(token));
        }
        String answer = sb.toString();
        return answer;
    }
}