import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {

            Queue<Integer> q = new LinkedList<>();
            ArrayList<Integer> ans = new ArrayList<>();
            int idx=0;

            for (int each : progresses) {
                q.add(each);
            }

            while (!q.isEmpty()) {
                int cnt = 0;

                for (int i = 0; i < progresses.length; i++) {
                    progresses[i] += speeds[i];
                }

                while (!q.isEmpty() && progresses[idx] >= 100) {
                    q.poll();
                    cnt++;
                    idx++;
                }

                if (cnt > 0) {
                    ans.add(cnt);
                }
                
                }

            int[] last = new int[ans.size()];

            int cnt=0;

            for (int each : ans) {
                last[cnt] = each;
                cnt++;
            }

            return last;

            }

        }