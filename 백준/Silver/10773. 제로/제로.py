def solution():
    
    N = int(input())

    lis = []

    for i in range(N):
        num = int(input())

        if num == 0:
            lis.pop()
        else :
            lis.append(num)

    print(sum(lis))

solution()