def solution():

    N = int(input())

    num_list = [ input() for i in range(N)]

    for word in num_list:
        temp_word=""
        for i,char in enumerate(word):
            if temp_word =="":
                temp_word +=char
            elif word[i] != word[i-1]:
                temp_word += char

        print(temp_word)

solution()