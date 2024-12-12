def sol():
    Num = int(input())
    
    arr=[-1] * (Num+2)
    arr[0]=0
    arr[1]=1
    
    for i in range(2,Num+1):
        arr[i]=arr[i-2]+arr[i-1]
        
    print(arr[Num])
    
sol()