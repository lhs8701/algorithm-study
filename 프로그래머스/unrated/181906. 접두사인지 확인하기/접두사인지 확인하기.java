class Solution {
    public int solution(String my_string, String is_prefix) {
        return my_string.substring(0, Math.min(is_prefix.length(), my_string.length())).equals(is_prefix) ? 1 : 0;
    }
}