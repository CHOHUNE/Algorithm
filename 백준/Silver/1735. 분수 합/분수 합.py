def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def sol():
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    
    N = a*d + b*c 
    M = b*d
    
    GCD=gcd(N,M)

    print(N//GCD,M//GCD)
sol()