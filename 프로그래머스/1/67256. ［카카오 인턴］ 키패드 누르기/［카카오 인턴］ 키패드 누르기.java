import java.util.*;
class Solution {
    
    int[][] array = new int[][]{{3, 2, 1, 0}, {1, 2, 3, 4}, {0, 1, 2, 3}, {1, 2, 3, 4}, 
                                  {2, 1, 2, 3}, {1, 0, 1, 2}, {2, 1, 2, 3}, {3, 2, 1, 2}, 
                                  {2, 1, 0, 1},{3, 2, 1, 2}, {4, 3, 2, 1}, {4, 3, 2, 1}};
    Map<Integer, Integer> convertMap = Map.of(2, 0, 5, 1, 8, 2, 0, 3);
    Map<String, Integer> pointerMap = new HashMap<>();
    String[] handMap = new String[]{"?", "L", "?", "R", "L", "?", "R", "L", "?", "R"};
    
    public String solution(int[] numbers, String hand) {
        String answer = "";
        pointerMap.put("L", 10);
        pointerMap.put("R", 11);
        
        for(int number : numbers){
            String str = handMap[number];
            if (str.equals("?")){
                str = get(number, hand);
            }
            pointerMap.put(str, number);
            answer += str;
        }
        return answer;
    }
    
    private String get(int number, String hand){
        int v = convertMap.get(number);
        int l = pointerMap.get("L");
        int r = pointerMap.get("R");
        if (array[l][v] < array[r][v]){
            return "L";
        }
        if (array[l][v] > array[r][v]){
            return "R";
        }
        if (hand.equals("left")){
            return "L";
        }
        return "R";
    }
}
        // 1,3 -> 2 : 1
        //     -> 5 : 2
        //     -> 8 : 3
        //     -> 0 : 4
        // 4,6 -> 2 : 2
        //     -> 5 : 1
        //     -> 8 : 2
        //     -> 0 : 3
        // 7,9 -> 2 : 3
        //     -> 5 : 2
        //     -> 8 : 1
        //     -> 0 : 2
        // 2   -> 2 : 0
        //     -> 5 : 1
        //     -> 8 : 2
        //     -> 0 : 3
        // 5   -> 2 : 1
        //     -> 5 : 0
        //     -> 8 : 2
        //     -> 0 : 3
        // 8   -> 2 : 2
        //     -> 5 : 1
        //     -> 8 : 0
        //     -> 0 : 1
        // 0   -> 2 : 3
        //     -> 5 : 2
        //     -> 8 : 1
        //     -> 0 : 0

