def gcd(a,b):

    if b==0:
        return a
    return gcd(b,a%b)

def sol():
    N= int(input())
    for i in range(N):
        a,b = map(int,input().split())
        
        num = gcd(a,b)
        print((a*b)//num)
        
sol()