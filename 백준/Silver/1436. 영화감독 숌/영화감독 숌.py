def sol():
    ans=666
    count=int(input())
    num=0
    while True:
        if '666' in str(ans):
            num+=1
            if num==count:
                print(ans)
                break
        ans+=1

sol()
    
    