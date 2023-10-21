import java.util.stream.*;

class Solution {
    public String[] solution(String[] names) {
        return IntStream.range(0, names.length)
            .filter(idx -> idx % 5 == 0)
            .mapToObj(idx -> names[idx])
            .toArray(String[]::new);
    }
}