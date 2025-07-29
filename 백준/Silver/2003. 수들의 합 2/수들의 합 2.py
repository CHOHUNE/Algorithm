def solution():

    N,M = map(int,input().split())
    num = list(map(int,input().split()))

    ans=0
    for i in range(N):
        cnt =0
        for j in range(i,N):
            cnt+=num[j]
            if(cnt == M):
                ans+=1

    print(ans)
solution()

