def solution():

    num =int(input())
    coordinates = [list(map(int, input().split())) for _ in range(num)]
    answer =[int(1e9)] *num


    for x in coordinates :
        for y in coordinates :
            costs=[]
            for ix, iy in coordinates:
                costs.append(abs(x[0]-ix)+abs(y[1]-iy))

            costs.sort()
            cost=0
            for i in range(num):
                cost+=costs[i]
                answer[i]=min(answer[i],cost)
    print(*answer)

solution()

