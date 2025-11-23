def solution():

    N =int(input())


    lis = [ tuple(map(int,input().split())) for _ in range(N)]

    lis.sort(key = lambda x : (x[1] , x[0]))

    for x,y in lis:

        print(x,y,sep=' ')

solution()
