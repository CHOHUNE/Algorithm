def parametric(trees,mid,M):

    total =0 
    for tree in trees:

        if tree > mid:
            total += tree - mid

    return total >= M        


def solution():

    N , M = map(int,input().split())
    trees = list(map(int,input().split()))

    left = 0            # 아무 것도 안자르는 경우
    right= max(trees)   # 최대 : 가장 높은 나무

    answer = 0

    while  left <= right:
        mid = (left + right) // 2

        if parametric(trees, mid, M): # M은 가져야 하는 나무 높이(target)
            answer = mid 
            left = mid + 1
        else :
            right = mid -1 

    print(answer)

solution()

