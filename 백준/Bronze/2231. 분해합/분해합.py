def sol():
    num =int(input())
    
    for i in range(num):

        ans = i + sum(map(int,str(i)))
        if ans==num:
            print(i)
            return
        
    print(0)
sol()