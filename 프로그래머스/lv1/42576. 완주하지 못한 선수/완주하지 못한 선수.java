import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.groupingBy;
import static java.util.stream.Collectors.counting;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);
        Arrays.sort(completion);
        for(int i=0, n=completion.length; i<n; i++){
            if (!participant[i].equals(completion[i])){
                return participant[i];
            }
        }
        return participant[participant.length - 1];
    }
}