def sol():

    while True:
        num = int(input())
        ans=[]
        
        if num==-1 :
            break
        for i in range(1,num+1):
            if num%i==0:
                ans.append(i)
        divisor= sum(ans[:len(ans)-1])
        if num==divisor:
            print(num,end=' = ')
            print(' + '.join(map(str,ans[:len(ans)-1])))
        else: 
            print(str(num) + " is NOT perfect.")
sol()