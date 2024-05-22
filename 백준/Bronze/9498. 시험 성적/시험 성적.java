import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args)throws IOException{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer str= new StringTokenizer(br.readLine(), " ");
        
        int a = Integer.parseInt(str.nextToken());
        
        if(a>=90){
          System.out.println("A");  
        } 
        else if(a>=80){
          System.out.println("B");  
        } 
        else if(a>=70){
          System.out.println("C");  
        } 
       else if(a>=60){
         System.out.println("D");  
       }else{
          System.out.println("F");  
        } 
    }
}

//시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F
// 시험 점수 0~ 100 

