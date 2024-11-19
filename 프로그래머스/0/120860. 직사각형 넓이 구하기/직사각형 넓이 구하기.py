def solution(dots):
    x =[point[0] for point in dots]
    y =[point[1] for point in dots]
    
    x_values=0
    if min(x)==0 :
        x_values=max(x)
    elif min(x)>0 :
        x_values=max(x)-min(x)
    elif min(x)<0 :
        x_values=max(x)+abs(min(x))
    
    if min(y)==0 :
        y_values=max(y)
    elif min(y)>0 :
        y_values=max(y)-min(y)
    elif min(y)<0 :
        y_values=max(y)+abs(min(y))
        
    return x_values*y_values