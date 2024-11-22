
def solution(my_string):
    ans=''
    for each in my_string :
        if not each in ans :
            ans+=each
    return ans