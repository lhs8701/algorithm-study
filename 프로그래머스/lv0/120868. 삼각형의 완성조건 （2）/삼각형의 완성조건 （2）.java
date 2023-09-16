class Solution {
    public int solution(int[] sides) {
        int large = (sides[0] < sides[1]) ? sides[1] : sides[0];
        int small = (sides[0] < sides[1]) ? sides[0] : sides[1];
        // large <= biggest < large + small 
        // large < x + small
        // large - small < x < large
       
        return (large - (large - small) - 1) + (large + small - large);
    }
}