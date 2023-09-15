import java.util.*;
class Solution {
    public String solution(String my_string) {
        Set<String> set = new LinkedHashSet<>(Arrays.asList(my_string.split("")));
        StringBuilder sb = new StringBuilder();
        for(String str: set){
            sb.append(str);
        }
        String answer = sb.toString();
        return answer;
    }
}