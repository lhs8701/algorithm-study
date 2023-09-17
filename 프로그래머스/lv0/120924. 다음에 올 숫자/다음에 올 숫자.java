class Solution {
    public int solution(int[] common) {
        int last = common[common.length - 1];
        return common[1] - common[0] == common[2] - common[1] ? last + common[1] - common[0] : last * common[1] / common[0];
    }
}