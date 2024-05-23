import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args)throws IOException{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));        


        
        int a = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for(int i =0 ; i<a ; i++){
            sb.append("*");
           bw.write(sb.toString()+"\n");
        }
        
        br.close();
        bw.close();
    }
}