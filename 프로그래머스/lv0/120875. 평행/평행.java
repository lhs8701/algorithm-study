import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[][] dots) {
        return gradient(dots, 0, 1) == gradient(dots, 2, 3) || 
            gradient(dots, 0, 2) == gradient(dots, 1, 3) || 
            gradient(dots, 0, 3) == gradient(dots, 1, 2) ? 1 : 0;
    }
    
    public double gradient(int[][] dots, int i, int j){
        return (dots[i][0] - dots[j][0]) * 1.0 / (dots[i][1] - dots[j][1]);
    }
}