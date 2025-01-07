import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer>list = new ArrayList<>();
        int cnt=0;
        for(int eachNum : arr){

            if (list.isEmpty()) {
                list.add(eachNum);
            }else if(list.get(cnt) != eachNum) {
                list.add(eachNum);
                cnt++;
            }
        }


        int[] answer = new int[list.size()];
        cnt = 0;
        for (int Each : list) {
            answer[cnt] = Each;
            cnt++;
        }

        return answer;
    }
}