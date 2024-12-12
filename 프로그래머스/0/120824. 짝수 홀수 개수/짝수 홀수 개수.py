def solution(num_list):
    cnt1=0
    cnt2=0
    for i in num_list:
        if i %2==0 :
            cnt1+=1
        else :
            cnt2+=1
    return [cnt1,cnt2]