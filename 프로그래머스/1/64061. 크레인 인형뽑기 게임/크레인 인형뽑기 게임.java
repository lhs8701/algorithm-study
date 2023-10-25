import java.util.*;
class Solution {
    public int solution(int[][] board, int[] moves) {
        int N = board.length;
        int answer = 0;
        List<Deque<Integer>> list = new ArrayList<>();
        Deque<Integer> bucket = new ArrayDeque<>();
        for(int i=0; i<N; i++){
            list.add(new ArrayDeque<>());
        }
        
        for(int i=N-1; i>=0; i--){
            for(int j=0; j<N; j++){
                list.get(j).push(board[i][j]);
            }
        }
    
        for(int move : moves){
            Deque<Integer> stack = list.get(move-1);
            while(!stack.isEmpty() && stack.peek() == 0){
                stack.pop();
            }
            if (!stack.isEmpty()){
                bucket.push(stack.pop());                
            }
            if (bucket.size() > 1){
                int second = bucket.pop();
                int first = bucket.pop();
                answer += 2;
                if (second != first){
                    bucket.push(first);
                    bucket.push(second);
                    answer -= 2;
                }
            }
        }
        return answer;
    }
}