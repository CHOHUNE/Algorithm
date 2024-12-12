def sol(x):
    global arr
    
    if arr[x] != -1:   # 배열의 x번째 값을 검사
        return arr[x]
    arr[x] = sol(x-1) + sol(x-2)
    return arr[x]

N = int(input())
arr = [-1]*(N+2)
arr[0] = 0
arr[1] = 1

print(sol(N))