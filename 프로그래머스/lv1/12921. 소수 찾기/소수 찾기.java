import java.util.*;
import java.util.stream.*;

class Solution {
    boolean[] isPrime = new boolean[1000001];
    public int solution(int n) {
        init();
        return (int)IntStream.rangeClosed(1, n)
            .filter(i -> isPrime[i])
            .count();
    }
    
    public void init(){
        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        isPrime[1] = false;
        
        for(int i=2; i*i<=1000000; i++){
            for(int j=i*i; j<=1000000; j+=i){
                isPrime[j] = false;
            }
        }
    }
}