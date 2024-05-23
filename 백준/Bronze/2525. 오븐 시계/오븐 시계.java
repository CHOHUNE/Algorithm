import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader( new InputStreamReader(System.in));
        
        StringTokenizer str1 = new StringTokenizer(br.readLine(), " "); 
        int a1 = Integer.parseInt(str1.nextToken());
        int a2 = Integer.parseInt(str1.nextToken());        
        
        StringTokenizer str2 = new StringTokenizer(br.readLine(), " ");         
        int a3 = Integer.parseInt(str2.nextToken());
        
        int min = a1*60+a2+a3;
        
        int hour=(min/60)%24;
        int minutes=min%60;
        
        System.out.println(hour+" "+minutes);
        
        br.close();
    }
    }


//예제 입력 3 
//23 48
//25

//예제 출력 3 
//0 13