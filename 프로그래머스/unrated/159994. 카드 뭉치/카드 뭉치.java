import java.util.*;

class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        Deque<String> stack1 = new ArrayDeque<>(Arrays.asList(cards1));
        Deque<String> stack2 = new ArrayDeque<>(Arrays.asList(cards2));
        for(String str : goal){
            if (str.equals(stack1.peek())){
                stack1.pop();
            }
            else if (str.equals(stack2.peek())){
                stack2.pop();
            }
            else{
                return "No";
            }
        }
        return "Yes";
    }
}