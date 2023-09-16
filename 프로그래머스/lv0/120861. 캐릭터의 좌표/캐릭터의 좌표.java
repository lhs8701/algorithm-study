class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int x = 0;
        int y = 0;
        for(String str: keyinput){
            if (str.equals("up") && y < board[1]/2){
                y +=1;
            }
            else if (str.equals("down") && -board[1]/2 < y){
                y -=1;
            }
            else if (str.equals("right") && x < board[0]/2){
                x += 1;
            }
            else if (str.equals("left") && -board[0]/2 < x){
                x -= 1;
            }
        }
        return new int[]{x, y};
    }
}