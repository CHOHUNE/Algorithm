def sol(index, level):
    global arr, choose, k 
    
    if level ==6 :
        for p in choose:
            print(p, end=' ')
 
        print()
        return
    
    for i in range(index,k):
        choose.append(arr[i])
        sol(i+1,level+1)
        choose.pop()
    
while True:
    choose = [] 
    lst = list(map(int,input().split()))
    k = lst[0]
    arr = lst[1:]
    
    if k == 0:
        break
    
    sol(0,0)
    print()
    