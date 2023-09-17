class Solution {
    public int solution(String A, String B) {
        int length = A.length();
        for(int i=0; i<length; i++){
            int idx = length - i;
            if (B.equals(A.substring(idx) + A.substring(0, idx))){
                return i;
            }
        }
        return -1;
    }
}