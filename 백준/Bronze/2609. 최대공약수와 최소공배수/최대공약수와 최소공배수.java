import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args)throws IOException{
        
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
       StringTokenizer str = new StringTokenizer(br.readLine());
        
        int a = Integer.parseInt(str.nextToken());
        int b = Integer.parseInt(str.nextToken());
        
        System.out.println(GCD(a,b));
        
        System.out.println((a*b)/GCD(a,b));
        
    }
    
    private static int GCD(int num1, int num2){
        
        if(num1%num2 ==0 )return num2;
        
      return GCD(num2, num1%num2);  
    }
}