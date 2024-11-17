def solution(arr):
    
    answer=0
    
    while True:
        prev_arr = arr.copy() #이전배열
        temp_arr =[] #새로운 배열 
        
        for i in arr :
            if i>50 and i%2 ==0 :
                temp_arr.append(i/2)
            elif i<50 and i%2 !=0 :
                temp_arr.append(i*2+1)
                
        if temp_arr == prev_arr : break;
                
        arr = temp_arr
        answer+=1
                
    return answer-1