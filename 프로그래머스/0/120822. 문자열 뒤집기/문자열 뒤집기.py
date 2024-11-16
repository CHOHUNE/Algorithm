def solution(my_string):
    idx = len(my_string)
    txt =""
    for i in range (idx-1,-1,-1):
        txt+=my_string[i]
    
    return txt