import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.util.StringTokenizer;

public class Main{
  public static void main(String[] args)throws IOException{


    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int a = Integer.parseInt(br.readLine());

    StringTokenizer str = new StringTokenizer(br.readLine());

  
    int ans=0;

    for(int i =0; i<a;i++){

      int temp = Integer.parseInt(str.nextToken());
      
      if(is_Prime(temp)) ans++;
    
    

    }

    System.out.println(ans);

  }

  private static boolean is_Prime(int Number){

    if(Number == 1){

      return false;
    }

    for(int i=2; i<Number;i++){
      if(Number% i ==0) return false;
    }


    return true;

  }


}
