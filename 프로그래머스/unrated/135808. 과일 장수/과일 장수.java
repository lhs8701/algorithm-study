import java.util.*;

class Solution {
    public int solution(int k, int m, int[] score) {
        int n = score.length / m;
        int r = score.length % m;
        int sum = 0;
        Arrays.sort(score);
        score = Arrays.copyOfRange(score, r, score.length);
        for(int i=0; i<score.length; i+=m){
            sum += score[i] * m;
        }
        return sum;
    }
}