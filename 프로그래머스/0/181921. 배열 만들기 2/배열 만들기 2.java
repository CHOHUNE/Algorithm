import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        int[] answer = {};
        
        ArrayList<Integer> arrayList = new ArrayList<>();
        
        for (int i=l; i<=r ; i++){
            if(String.valueOf(i).matches("[05]+")){
                arrayList.add(i);
            }
        }
        
        if(arrayList.isEmpty()){
            return new int[]{-1};
        }
        
        int [] a =new int[arrayList.size()];
        
        for(int j=0;j< arrayList.size();j++){
            a[j] = arrayList.get(j);
          }
        
        return a;
    }
}