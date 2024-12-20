import math
def get_divisors(n):
    num=int(math.sqrt(n))
    ans={1,n}
    for i in range(2,num+1):
        if n%i==0:
            ans.add(i)
            ans.add(n//i)
    return ans
    
def sol():
    N=int(input())
    for i in range(N):
        a,b= map(int,input().split())
        common_divisors=get_divisors(a)&get_divisors(b)
        if common_divisors:
            print((a*b)//max(common_divisors))
        else:
            print(a*b)
sol()
        