class Solution {
    public int solution(String my_string, String is_suffix) {
        return my_string.substring(Math.max(my_string.length() - is_suffix.length(), 0), my_string.length()).equals(is_suffix) ? 1 : 0;
    }
}