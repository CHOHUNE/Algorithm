import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args)throws IOException{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer str = new StringTokenizer(br.readLine(), " ");
        
        int a = Integer.parseInt(str.nextToken());
        int b = Integer.parseInt(str.nextToken());
        int c = Integer.parseInt(str.nextToken());
        
        int ans=0; 
        
        if(a==b &&b==c){
                
            ans= 10000+a*1000;
            System.out.println(ans);
        }else if(a==b){
            ans = 1000+a*100;
            System.out.println(ans);
        }else if(b==c){
            ans = 1000+b*100;
            System.out.println(ans);
        }else if(a==c){
            ans = 1000+a*100;
            System.out.println(ans);
        }else{
            ans=Math.max(Math.max(a,b),c)*100;
            System.out.println(ans);

        }
        
        br.close();
    }
}

//같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
//같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
//모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.