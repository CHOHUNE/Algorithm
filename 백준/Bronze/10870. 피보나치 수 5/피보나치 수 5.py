def sol(num):
    
    if num ==0:
        return 0
    if num ==1:
        return 1
   
    return sol(num-1)+sol(num-2)
        

    
num=int(input())
print(sol(num))