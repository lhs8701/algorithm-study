class Solution {
    public int solution(int a, int b) {
        int num1 = Integer.parseInt(a + "" + b);
        int num2 = Integer.parseInt(b + "" + a);
        return num1 > num2 ? num1 : num2;
    }
}