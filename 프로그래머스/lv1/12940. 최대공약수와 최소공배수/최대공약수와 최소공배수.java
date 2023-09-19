class Solution {
    public int[] solution(int n, int m) {
        int g = gcd(n, m);
        return new int[]{g, n*m/g};
    }
    
    public int gcd(int num1, int num2){
        int a = Math.max(num1, num2);
        int b = Math.min(num1, num2);
        System.out.println(a + b);
        
        while (b != 0){
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}