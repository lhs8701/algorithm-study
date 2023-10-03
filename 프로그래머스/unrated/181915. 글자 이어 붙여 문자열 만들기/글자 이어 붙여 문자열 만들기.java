import java.util.stream.*;

class Solution {
    public String solution(String my_string, int[] index_list) {
        String[] arr = my_string.split("");
        return IntStream.of(index_list)
            .mapToObj(i -> arr[i])
            .collect(Collectors.joining());
    }
}