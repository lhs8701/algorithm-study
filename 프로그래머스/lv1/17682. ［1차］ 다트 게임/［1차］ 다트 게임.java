import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(String dartResult) {
        int i=0;
        int j=0;
        String num = "";
        int[] arr = new int[3];
        String[] str = dartResult.split("");
        while (i<3){
            char c = dartResult.charAt(j++);
            if (Character.isDigit(c)){
                num += String.valueOf(c);
            }else{
                if (c == 'S'){
                    arr[i] = Integer.parseInt(num);
                    num = "";
                }
                else if (c == 'D'){
                    arr[i] = (int)Math.pow(Integer.parseInt(num), 2);
                    num = "";
                }
                else if (c == 'T'){
                    arr[i] = (int)Math.pow(Integer.parseInt(num), 3);
                    num = "";
                }
                else if (c == '*'){
                    arr[i] *= 2;
                    if (i > 0) {
                        arr[i-1] *= 2;
                    }
                }
                else if (c == '#'){
                    arr[i] *= -1;
                }
                if (dartResult.length() <= j || Character.isDigit(dartResult.charAt(j))){
                    i++;
                }
            }
        }
        return (int) IntStream.of(arr).sum();
    }
}