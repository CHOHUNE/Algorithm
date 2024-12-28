def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def sol():
    N= int(input())
    
    nums=[]
    for i in range(N):
        nums.append(int(input()))
        
    distances=[]
    for i in range(1,N):
        distances.append(nums[i]-nums[i-1])

    gap=distances[0]
    
    for i in range(1,len(distances)):
        gap= gcd(gap,distances[i])
        
    total=(nums[-1]-nums[0]) // gap + 1 
    
    need = total - N 
    
    print(need)
    
sol()
        
        