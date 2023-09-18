class Solution {
    public int solution(int num) {
        long r = num;
        for(int i=0; i< 500; i++) {
            if (r == 1){
                return i;
            }
            if (r % 2 == 0){
                r /= 2;
            }else{
                r = r * 3 + 1;
            }
            
        }
        return r == 1 ? 500 : -1;
    }
}