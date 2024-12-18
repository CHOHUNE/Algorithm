import math
def sol():
    min_num = int(input())
    max_num = int(input())
    
    arr = [True]*(max_num+1)
    
    arr[0]=arr[1]=False
    
    for x in range(2,int(math.sqrt(max_num))+1):
        if arr[x]:
            for y in range(x*x,max_num+1,x):
                arr[y]=False
                
    choose=[]
    for i in range(min_num,max_num+1):
        if arr[i]:
            choose.append(i)
            
    if choose:
        print(sum(choose))
        print(min(choose))
    else:
        print(-1)
sol()