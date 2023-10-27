import java.util.stream.*;
class Solution {
    public int solution(int n) {
        return n%2==1 ? IntStream.iterate(1, num -> num+2).limit((n+1)/2).sum()
            : IntStream.iterate(2, num -> num+2).limit(n/2).map(num -> num*num).sum();
    }
}