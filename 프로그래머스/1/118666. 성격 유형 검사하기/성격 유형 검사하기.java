import java.util.*;
class Solution {
    Map<String, Integer> map = Map.of("R", 0, "T", 1, "C", 2, "F", 3, "J", 4, "M", 5, "A", 6, "N", 7);
    int[] count = new int[]{0, 0, 0, 0, 0, 0, 0, 0};
    public String solution(String[] survey, int[] choices) {
        for(int i=0; i<survey.length; i++){
            String str = survey[i];
            String first = "" + str.charAt(0);
            String second = "" + str.charAt(1);
            switch(choices[i]){
                case 1:
                case 2:
                case 3:
                    count[map.get(first)] += 4 - choices[i];
                    break;
                default:
                    count[map.get(second)] += choices[i] - 4;
                    break;
            }
        }
        return compare("R","T") + compare("F", "C") + compare("M", "J") + compare("A", "N");
    }
    
    public String compare(String first, String second){
        if (count[map.get(first)] == count[map.get(second)]){
            return first.compareTo(second) < 0 ? first : second;
        }
        return count[map.get(first)] > count[map.get(second)] ? first : second;
    }
}