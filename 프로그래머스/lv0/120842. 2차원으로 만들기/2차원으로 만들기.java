class Solution {
    public int[][] solution(int[] num_list, int n) {
        int length = num_list.length;
        
        int[][] answer = new int[(int)(length/n)][n];
        System.out.println(length);
        for (int i=0; i<length; i++){
            answer[(int)(i / n)][i % n] = num_list[i];
        }
        return answer;
    }
}