def sol():
    N=int(input())
    
    n=1
    a=2
    for i in range(N):
        a+=n
        n*=2
    print(a**2)
sol()
        