class Solution {
    public String solution(String phone_number) {
        String[] array = phone_number.split("");
        String answer = "";
        for(int i=0, n=phone_number.length(); i<n; i++){
            answer += i < n - 4 ? "*" : array[i];
        }
        return answer;
    }
}