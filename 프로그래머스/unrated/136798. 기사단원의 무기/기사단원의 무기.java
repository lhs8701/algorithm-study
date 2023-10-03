import java.util.*;
import java.util.stream.*;

class Solution {
    int[] divisor = new int[100001];
    public int solution(int number, int limit, int power) {
        init();
        return IntStream.rangeClosed(1, number)
            .map(n -> divisor[n] > limit ? power : divisor[n])
            .sum();
    }
    
    public void init(){
        Arrays.fill(divisor, 1);
        for(int i=2; i<=100000; i++){
            for(int j=i; j<=100000; j+=i){
                divisor[j]++;
            }
        }
    }
}