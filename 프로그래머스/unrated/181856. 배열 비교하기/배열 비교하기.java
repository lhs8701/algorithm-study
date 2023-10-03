import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[] arr1, int[] arr2) {
        return arr1.length == arr2.length ? Integer.compare(Integer.valueOf(IntStream.of(arr1).sum()), Integer.valueOf(IntStream.of(arr2).sum())) : Integer.compare(Integer.valueOf(arr1.length), Integer.valueOf(arr2.length));
    }
}