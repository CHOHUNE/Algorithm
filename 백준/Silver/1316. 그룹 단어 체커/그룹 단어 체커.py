def solution():
    N = int(input())

    lis = [input() for i in range(N)]
    flag_word = True
    cnt = 0
    for word in lis:
        ans = []
        flag_word = True
        for i,char in enumerate(word):

            if char not in ans:
                ans.append(char)
            else:
                if word[i-1] != word[i]:
                    flag_word = False
                    break
            
        if flag_word:
            cnt+=1

    print(cnt)
            


solution()
