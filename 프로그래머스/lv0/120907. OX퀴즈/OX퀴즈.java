import java.util.*;
import java.util.stream.*;

class Solution {
    public String[] solution(String[] quiz) {
        return Arrays.stream(quiz)
            .map(str -> str.replaceAll(" - ", " -").replaceAll("--", "").replaceAll(" \\+ ", " ").replaceAll(" = ", " "))
            .map(str -> Arrays.stream(str.split(" ")).mapToInt(Integer::parseInt).toArray())
            .map(arr -> arr[0] + arr[1] == arr[2] ? "O" : "X")
            .toArray(String[]::new);
    }
}