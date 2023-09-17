import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[][] board) {
        int n = board.length;
        int[][]dir = new int[][]{{+1, +1}, {+1, 0}, {+1, -1}, {0, +1}, {0, -1}, {-1, +1}, {-1, 0}, {-1, -1}};
        
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if (board[i][j] == 1){
                    for (int k=0; k<8; k++){
                        int x = i + dir[k][0];
                        int y = j + dir[k][1];
                        if (0 <= x && x < n && 0 <= y && y < n && board[x][y] == 0){
                            board[x][y] = 2;
                        }
                    }
                }
            }
        }
        return (int)Arrays.stream(board).mapToLong(arr -> IntStream.of(arr).filter(num -> num == 0).count()).sum();
    }
}