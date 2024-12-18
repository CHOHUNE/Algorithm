
N = int(input())
check = [False]*(N+1)
choose=[]

def sol(level):
    if level == N:
        print(' '.join(map(str,choose)))
        return 

    for i in range(1,N+1):
        if check[i]==True:
            continue
        choose.append(i)
        check[i]=True
        sol(level+1)
        check[i]=False
        choose.pop()
    
sol(0)
