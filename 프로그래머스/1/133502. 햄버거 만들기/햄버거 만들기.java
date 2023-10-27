import java.util.*;
import java.util.stream.*;
class Solution {
    Deque<Integer> stack = new ArrayDeque<>();
    public int solution(int[] ingredient) {
        int sum = 0;
        for(int num : ingredient){
            stack.push(num);
            sum += check();
        }
        return sum;
    }
    public int check(){
        if (stack.size() > 3){
            int num4 = stack.pop();
            int num3 = stack.pop();
            int num2 = stack.pop();
            int num1 = stack.pop();
            if (num1 == 1 && num2 == 2 && num3 == 3 && num4 == 1){
                return 1;
            }
            stack.push(num1);
            stack.push(num2);
            stack.push(num3);
            stack.push(num4);
        }
        return 0;
    }
}