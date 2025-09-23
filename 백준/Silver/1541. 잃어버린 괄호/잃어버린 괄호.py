def solution():

    line = input().split("-")


    for i, value in enumerate(line):

        if "+" in value:
            line[i] = sum(map(int,value.split("+")))
        else:
            line[i] = int(value)    

    ans = line[0]
    if len(line) > 1:
        for i in range(1,len(line)):
            ans-= line[i]

    print(ans)

solution()
