import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
  public static void main(String[] args)throws IOException{

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer str = new StringTokenizer(br.readLine());

    int min = Integer.parseInt(str.nextToken());
    int max = Integer.parseInt(str.nextToken());

    boolean[] arr = new boolean[max+1];
    
    StringBuilder sb = new StringBuilder();

    arr[0] = true;
    arr[1] = true;



    

    for(int i= 2 ; i*i <=max ; i++){
      if(!arr[i]) {
        for(int j = i*i ; j<=max ; j+= i){

          arr[j]=true;
        }
      }

       }

       for( int i= min; i<= max;i++){

        if(!arr[i]) sb.append(i).append("\n");
       }

       System.out.println(sb);

      }
     
    
    }
