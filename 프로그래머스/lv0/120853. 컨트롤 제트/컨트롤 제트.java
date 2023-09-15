class Solution {
    public int solution(String s) {
        String[] token = s.split(" ");
        int size = token.length;
        
        int sum = 0;
        for(int i=0; i<size; i++){
            if (i > 0 && token[i].equals("Z")){
                sum -= Integer.parseInt(token[i-1]);
                continue;
            }
            int digit = Integer.parseInt(token[i]);
            sum += digit;
        }
        int answer = sum;
        return answer;
    }
}