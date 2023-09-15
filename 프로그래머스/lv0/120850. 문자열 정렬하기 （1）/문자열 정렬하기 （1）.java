import java.util.*;

class Solution {
    public int[] solution(String my_string) {
        String str = my_string.replaceAll("[a-z]","");
        char[] charArray = str.toCharArray();
        int[] answer = new int[charArray.length];
        for(int i=0, n=charArray.length; i<n; i++){
            answer[i] = charArray[i] - '0';
        }
        Arrays.sort(answer);
        return answer;
    }
}