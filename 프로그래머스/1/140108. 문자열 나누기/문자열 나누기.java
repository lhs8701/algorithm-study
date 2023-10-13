class Solution {
    public int solution(String s) {
        int answer = 0;
        while (!s.isEmpty()){
            char target = s.charAt(0);
            int count1 = 1;
            int count2 = 0;
            int i;
            int len = s.length();
            for(i = 1; i<len && count1 != count2; i++){
                if (target == s.charAt(i)){
                    count1++;
                }else{
                    count2++;
                }
            }
            s = s.substring(i);
            answer++;
        }
        return answer;
    }
}