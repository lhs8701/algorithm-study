import java.util.*;
import java.util.stream.*;
class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        return IntStream.range(0, n)
            .mapToObj(i -> Integer.toString(arr1[i] | arr2[i], 2))
            .map(str -> str.length() < n ? "0".repeat(n - str.length()) + str : str)
            .map(str -> Arrays.stream(str.split("")).map(ch -> ch.equals("1") ? "#" : " ").collect(Collectors.joining()))
            .toArray(String[]::new);
    }
}