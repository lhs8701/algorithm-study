class Solution {
    public int solution(String t, String p) {
        String[] arr = t.split("");
        int count = 0;
        int nLen = t.length();
        int pLen = p.length();
        for(int i=0; i<=nLen - pLen; i++){
            String num = "";
            for(int j=i; j<i+pLen; j++){
                num += arr[j];
            }
            if (Long.parseLong(num) <= Long.parseLong(p)){
                count++;
            }
        }
        return count;
    }
}