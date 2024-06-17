import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
  public static void main(String[] args)throws IOException{

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer str= new StringTokenizer(br.readLine());

    int a = Integer.parseInt(str.nextToken());
    int b = Integer.parseInt(str.nextToken());
    int c = Integer.parseInt(str.nextToken());
    
    int ans=0;

    int aPlus=0;
    int bPlus=0;
    int cPlus=0;

    while(true){

      aPlus++;
      bPlus++;
      cPlus++;

       ans++;
    
      if(aPlus ==16 ) aPlus =1;
      if(bPlus==29) bPlus=1;
      if(cPlus ==20) cPlus=1;

      if(a == aPlus && b== bPlus && c==cPlus){
        System.out.println(ans);
        break;
      }
      
      
    }
      
    
  }

}