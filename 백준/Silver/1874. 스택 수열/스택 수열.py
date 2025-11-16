def solution():
    
    ans = []
    N = int(input())
    print_ans =""
    current = 1
    
    for i in range(N):
        top = int(input())

        while current <= top:
            ans.append(current)
            print_ans +="+"
            current +=1
        if ans[-1] == top:
            ans.pop()
            print_ans+="-"
        else:
            print("NO")
            return
        
    print(*print_ans,sep='\n')
solution()
            
            
    
    