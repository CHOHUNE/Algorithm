import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args)throws IOException{
        
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(System.out));
       int d= Integer.parseInt(br.readLine());
        
        for(int i=0; i<d ; i++){
            StringTokenizer str = new StringTokenizer(br.readLine()," ");
            
            int ans =Integer.parseInt(str.nextToken())+Integer.parseInt(str.nextToken());
    
            bw.write(ans+"\n");
        }
 
        br.close();
        bw.flush();
        bw.close();
    }
}