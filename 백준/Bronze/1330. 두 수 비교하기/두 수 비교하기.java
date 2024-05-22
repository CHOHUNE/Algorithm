 import java.util.*;
 import java.io.*;

public class Main{
    public static void main (String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer str = new StringTokenizer(br.readLine(), " ");
        
        int a = Integer.parseInt(str.nextToken());
        
        int b = Integer.parseInt(str.nextToken());
        
        if(a>b)  System.out.println(">");
        if(a<b)  System.out.println("<");        
        if(a==b)  System.out.println("==");      
        
        br.close();
    }
}