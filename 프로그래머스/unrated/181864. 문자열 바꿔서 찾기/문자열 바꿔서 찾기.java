class Solution {
    public int solution(String myString, String pat) {
        myString = myString.replace("A","C");
        myString = myString.replace("B","D");
        myString = myString.replace("C","B");
        myString = myString.replace("D","A");
        return myString.contains(pat) ? 1 : 0;
    }
}