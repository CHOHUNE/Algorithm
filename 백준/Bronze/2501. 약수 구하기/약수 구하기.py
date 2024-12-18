def sol():
    a,b = map(int,input().split())
    
    ans = set()
    
    for i in range(1,a+1):
        if a%i ==0:
            ans.add(i)
    ans=list(ans)
    ans.sort()
    
    if b> len(ans):
        print(0)

    else :
        print(ans[b-1])
sol()
      