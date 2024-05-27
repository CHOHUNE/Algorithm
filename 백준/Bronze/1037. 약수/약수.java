import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());

        StringTokenizer str = new StringTokenizer(br.readLine(), " ");

        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;

        // 주어진 수들을 배열에 저장
        int arr[] = new int[num];

        for (int i = 0; i < num; i++) {
            arr[i] = Integer.parseInt(str.nextToken());

            // 가장 작은 약수와 가장 큰 약수를 구함
            max = Math.max(max, arr[i]);
            min = Math.min(min, arr[i]);
        }
        
        // 가장 작은 약수와 가장 큰 약수를 곱해 원래의 수를 찾음
        System.out.println(min * max);
    }
}
