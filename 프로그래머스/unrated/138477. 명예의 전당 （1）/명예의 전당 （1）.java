import java.util.*;
import java.util.PriorityQueue;
import java.util.stream.*;
class Solution {
    public int[] solution(int k, int[] score) {
        List<Integer> list = new ArrayList<>();
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int num : score){
            if (minHeap.size() < k){
                minHeap.add(num);
            }else{
                minHeap.add(num);
                minHeap.remove();
            }
            list.add(minHeap.peek());
        }
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}