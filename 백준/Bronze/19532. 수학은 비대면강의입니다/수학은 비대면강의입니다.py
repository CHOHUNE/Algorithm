def solution():
    # 입력받기: Ax + By = C와 Dx + Ey = F 형태의 연립방정식
    A, B, C, D, E, F = map(int, input().split())
    
    # -10000부터 10000까지 모든 x, y 값에 대해 검사
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            # 두 방정식을 동시에 만족하는지 확인
            if A*x + B*y == C and D*x + E*y == F:
                print(x, y)
                return  # 해를 찾으면 즉시 종료
    
solution()