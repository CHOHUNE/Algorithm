def solve():
    N = int(input())
    x=[]
    y=[]
    for i in range(N):
        x_each, y_each = map(int,input().split())
        x.append(x_each+50_0000)
        y.append(y_each+50_0000)
        
    ver_sum=[0]*(100_0000+1)
    ho_sum=[0]*(100_0000+1)
    
    for i in range(N):
        x1,y1=x[i],y[i]
        x2,y2=x[(i+1)%N],y[(i+1)%N]
        
        if x1==x2:
            start,end = min(y1,y2),max(y1,y2)
            ver_sum[start]+=1
            ver_sum[end]-=1
        else: 
            start,end=min(x1,x2),max(x1,x2)
            ho_sum[start]+=1
            ho_sum[end]-=1
            
    current=0
    max_ver=0
    
    for i in range(100_0000):
        current+=ver_sum[i]
        max_ver= max(max_ver,current)
        
    max_ho=0
    current=0
    for i in range(100_0000):
        current+=ho_sum[i]
        max_ho=max(max_ho,current)
    print(max(max_ho,max_ver))
    
solve()
        