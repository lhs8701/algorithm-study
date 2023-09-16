import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String[] id_pw, String[][] db) {
        Optional<String[]> element = Arrays.stream(db)
            .filter(arr -> arr[0].equals(id_pw[0]))
            .findFirst();
        if (element.isEmpty()){
            return "fail";
        }
        if (element.get()[1].equals(id_pw[1])){
            return "login";
        }
        return "wrong pw";
    }
}