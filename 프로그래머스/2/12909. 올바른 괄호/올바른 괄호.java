class Solution {
    boolean solution(String s) {
            boolean answer = false;


            char[] each = s.toCharArray();
            
            int idx= 0;

            for (char spell : each) {
                if (spell == ')') {
                    idx--;
                }
                 else if (spell == '(' ) {
                    idx++;
                }
                 
                 if(idx<0) {
                     return false;
                 }
               
            }

            if (idx == 0) {
                answer = true;
            }

            return answer;
        }
}