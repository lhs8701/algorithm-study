import java.util.stream.*;
class Solution {
    public int[] solution(int[] answers) {
        int sum1 = 0;
        int sum2 = 0;
        int sum3 = 0;
        int[] arr1 = new int[]{1, 2, 3, 4, 5};
        int[] arr2 = new int[]{2, 1, 2, 3, 2, 4, 2, 5};
        int[] arr3 = new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        for(int i=0; i<answers.length; i++){
            if (arr1[i % arr1.length] == answers[i]){
                sum1++;
            }
            if (arr2[i % arr2.length] == answers[i]){
                sum2++;
            }
            if (arr3[i % arr3.length] == answers[i]){
                sum3++;
            }
        }
        int[] answer = new int[]{sum1, sum2, sum3};
        int maxVal = IntStream.of(answer)
            .max()
            .getAsInt();
        return IntStream.of(1, 2, 3)
            .filter(i -> answer[i-1] == maxVal)
            .toArray();
    }
}