import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        return Arrays.stream(commands)
                .mapToInt(command -> IntStream.rangeClosed(command[0] - 1, command[1] - 1)
                        .boxed()
                        .sorted(Comparator.comparingInt(a -> array[a]))
                        .mapToInt(idx -> array[idx])
                        .toArray()[command[2] - 1]
                )
                .toArray();
    }
}