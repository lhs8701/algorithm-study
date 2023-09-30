import java.util.*;

class Solution {
    boolean[] isPrime = new boolean[3001];
    
    public int solution(int[] nums) {
        int answer = 0;
        init();
        for(int i=0; i<nums.length-2; i++){
            for(int j=i+1; j<nums.length-1; j++){
                for(int k=j+1; k<nums.length; k++){
                    int sum = nums[i] + nums[j] + nums[k];
                    if (isPrime[sum]){
                        answer++;
                    }
                }
            }
        }
        return answer;
    }
    
    public void init(){
        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        isPrime[1] = false;
        for(int i=2; i*i <= 3000; i++){
            for(int j = i*i; j<=3000; j+=i){
                isPrime[j] = false;
            }
        }
    }
}