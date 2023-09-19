import java.util.*;
import java.util.stream.*;
class Solution {
    public int solution(int[][] sizes) {
        int rMax = Arrays.stream(sizes).mapToInt(arr -> arr[0]).max().getAsInt();
        int cMax = Arrays.stream(sizes).mapToInt(arr -> arr[1]).max().getAsInt();
        
        if (rMax > cMax){
            return rMax * IntStream.range(0, sizes.length).map(i -> Math.min(sizes[i][0], sizes[i][1])).max().getAsInt();
        }else{
            return cMax * IntStream.range(0, sizes.length).map(i -> Math.min(sizes[i][0], sizes[i][1])).max().getAsInt();
        }
    }
}