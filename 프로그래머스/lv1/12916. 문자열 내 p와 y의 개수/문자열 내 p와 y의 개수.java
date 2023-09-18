import java.util.*;

class Solution {
    boolean solution(String s) {
        return s.replaceAll("p|P", "").length() == s.replaceAll("y|Y", "").length();
    }
}