import math
def sol():
    N=int(input())
    min=2
    max=math.sqrt(N)
    while min<=max:
        while N%min==0:
            print(min)
            N//=min
        min+=1
    if N>1:
        print(N)
sol()