import java.util.*;
class Solution {
    public int solution(String t, String p) {
            int cnt = 0;

            long pNum = Long.parseLong(p);

            for (int i = 0; i <= t.length() - p.length(); i++) {

                long tempNum = Long.parseLong(t.substring(i, i+p.length()));

                if (pNum >= tempNum) {
                    cnt++;
                }
            }
        return cnt;
    }
}