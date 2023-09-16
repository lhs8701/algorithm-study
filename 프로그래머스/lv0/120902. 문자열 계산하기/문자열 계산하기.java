import java.util.*;

class Solution {
    public int solution(String my_string) {
        String[] array = my_string.split(" ");
        int sum = Integer.parseInt(array[0]);
        
        for(int i=1, n = array.length; i < n - 1; i++){
            if (array[i].equals("+")){
                sum += Integer.parseInt(array[i + 1]);
            }
            else if (array[i].equals("-")){
                sum -= Integer.parseInt(array[i + 1]);
            }
        }
        
        return sum;
    }
}