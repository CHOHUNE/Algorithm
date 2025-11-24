
import sys
input = sys.stdin.readline

def rounding(N):
    if N >= 0:
        return int(N+0.5)
    else:
        return int(N-0.5)

def solution():


    N= int(input())
    lis = sorted([ int(input()) for _ in range(N)])
    
    cnt = {}
    for each in lis:
        cnt[each] = cnt.get(each,0) + 1

    
    mins = max(cnt.values()) 
    keys = [ key for key, value in cnt.items() if value == mins]
    keys.sort()


    #문제1 : 평균 
    print(rounding(sum(lis)/N))
    

    #문제2 : 중앙 값 

    print(lis[(N//2)]) # 무조건 홀수 -> 7 -> 7//2 =3 0123  중앙 값 

    #문제3 : 최빈 값 -> 2개 이상일 경우 두 번째로 작은 값 
    
    if len(keys) >=2:
        print(keys[1])
    else:
        print(keys[0])

    #문제4 : 최댓값과 최소값 차이 
    print(max(lis)-min(lis))
    

    

solution()