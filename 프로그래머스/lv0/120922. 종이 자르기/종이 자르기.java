class Solution {
    public int solution(int M, int N) {
        int large = Math.max(M, N);
        int small = Math.min(M, N);
        return (large - 1) + large * (small - 1);
    }
}