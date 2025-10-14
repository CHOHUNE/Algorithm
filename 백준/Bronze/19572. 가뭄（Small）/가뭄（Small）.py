def solution():
    num_list = list(map(int,input().split()))

    sum_num = sum(num_list)/2

    a = sum_num - num_list[0]
    b = sum_num - num_list[1]
    c = sum_num - num_list[2]

    if (a+b+c) == sum_num:
        if a >1 and b>1 and c>1:
            print(1)
            print(c,b,a)
        else:
            print(-1)
    else:
        print(-1)



solution()



