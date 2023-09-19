import java.util.*;
import java.util.stream.*;

class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int r = arr1.length;
        int c = arr1[0].length;
        return IntStream.range(0, r)
            .mapToObj(i -> IntStream.range(0, c).map(j -> arr1[i][j] + arr2[i][j]).toArray())
            .toArray(int[][]::new);
    }
}