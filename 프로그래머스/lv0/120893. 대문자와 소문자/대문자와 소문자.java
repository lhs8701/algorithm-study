class Solution {
    public String solution(String my_string) {
        String[] arr = my_string.split("");
        StringBuilder sb = new StringBuilder();
        for(String str : arr){
            if (str.equals(str.toLowerCase())){
                sb.append(str.toUpperCase());
            }else{
                sb.append(str.toLowerCase());
            }
        }
        String answer = sb.toString();
        return answer;
    }
}