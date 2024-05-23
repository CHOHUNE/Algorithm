import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args)throws IOException{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int num = Integer.parseInt(br.readLine());
        
        num/=4;
        StringBuilder sb= new StringBuilder();
        for(int i =0;i<num;i++){
            sb.append("long ");
        }
        
        
        
        System.out.println(sb.toString()+"int");
        
    }
}