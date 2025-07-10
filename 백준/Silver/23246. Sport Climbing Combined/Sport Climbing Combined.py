def solution():
    N=int(input())
    num_list=[]
    for i in range(N) :
        num_list.append(list(map(int,input().split())))

    num_list=sorted(num_list, key=lambda x:(x[1] * x[2] * x[3],x[1] + x[2] +x[3],x[0]))

    for x,y,z,b in num_list[:3]:
        print(x,end=' ')
        
solution()