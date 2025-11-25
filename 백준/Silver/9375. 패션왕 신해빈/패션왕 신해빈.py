from collections import defaultdict

def solution():

    T = int(input())

    for _ in range(T):

        num = int(input())
        lis = [input().split() for _ in range(num)]
    
        categories = {}

        for item, category in lis:
            categories.setdefault(category, 0)
            categories[category] += 1
            
        ans = list(categories.values())

        # ⚠ 의상이 0개일 경우 -> 아무것도 입을 수 없음
        if not ans:
            print(0)
            continue

        # 경우의 수 계산
        result = 1
        for c in ans:
            result *= (c + 1)

        print(result - 1)

solution()
