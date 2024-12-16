def sol():
    num = int(input())
    arr=[]
    for three in range((num//3)+1):
        for five in range((num//5)+1):
            if 3*three + 5*five ==num:
                arr.append(five+three)
    if not arr :
        print(-1)
        return
    print(min(arr))
sol()
                