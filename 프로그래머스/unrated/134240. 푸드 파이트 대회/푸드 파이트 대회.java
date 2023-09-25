class Solution {
    public String solution(int[] food) {
        String prefix = "";
        String postfix = "";
        for(int i=1; i<food.length; i++){
            prefix = prefix + String.valueOf(i).repeat(food[i]/2);
            postfix = String.valueOf(i).repeat(food[i]/2) + postfix;
        }
        return prefix + "0" + postfix;
    }
}