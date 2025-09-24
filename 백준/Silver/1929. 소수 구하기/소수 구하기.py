def solution():
    
    N,M = map(int,input().split())
    lis = [True] * (M+1)
    lis[0]=lis[1]=False
    
    for i in range(2,int(M**0.5)+1):
        if lis[i]:
            for j in range(i*i,M+1,i):
                lis[j] = False
    for i in range(N,M+1):
        if lis[i]:
            print(i)

solution()



# 에라토테네스의 체에서 중요한 건 제곱근 까지만 살펴본 후
# 해당 i 가 소수이면
# 소수의 배 만큼 False 
# 전부 True 로 만드는 것도 포인트 