class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        int n = gcd(a, b);
        int num = b / n;
        while (num != 1){
            if (num % 2 == 0){
                num /= 2;
            }
            else if (num % 5 == 0){
                num /= 5;   
            }else{
                return 2;
            }
        }
        return 1;
    }
    
    public int gcd(int num1, int num2){
        int a = Math.max(num1, num2);
        int b = Math.min(num1, num2);
        while (b != 0){
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}