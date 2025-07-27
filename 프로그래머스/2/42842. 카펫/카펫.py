def solution(brown, yellow):
    total = brown+ yellow
    ans =[]
    for height in range(3,int(total**0.5)+1):
        if (total % height) == 0:
            width = total // height
            
            if width >= height:
                inner_yellow = (width-2)*(height-2)
                
                if inner_yellow == yellow :
                    ans.append(width)
                    ans.append(height)
                    
    return ans