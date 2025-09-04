def solution(want, number, discount):
    compare= []
    for i in range(len(want)):
        compare.extend([want[i]]*number[i])
    compare.sort()
    # print("comapre",compare)
    temp=[]
    cnt=0
    
    for i in range(0,len(discount)-9):
        temp=discount[i:i+10]
        temp.sort()
        # print("tmep",temp)
        if temp == compare:
            cnt+=1

        
    return cnt