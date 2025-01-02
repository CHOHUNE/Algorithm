def sol():
    N=int(input())
    
    line = 1
    
    while N>line :
        N -=line
        line +=1
        
    if line % 2==0:
        n = N
        m = line - N +1 
    else : 
        n = line -N +1
        m = N
        
    print(str(n)+"/"+str(m))
    
sol()