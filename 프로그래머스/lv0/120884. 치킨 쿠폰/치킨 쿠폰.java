class Solution {
    public int solution(int chicken) {
        int n = chicken;
        int r = 0;
        int sum = 0;
        while (n >= 1){
            int temp1 = (n + r) / 10;
            int temp2 = (n + r) % 10;
            n = temp1;
            r = temp2;
            sum += n;
        }
        return sum;
    }
}