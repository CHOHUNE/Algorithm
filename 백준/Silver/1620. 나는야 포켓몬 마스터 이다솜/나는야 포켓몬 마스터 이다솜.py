import sys



def solution():

    L,M = map(int,input().split())
    int_dict  = {}
    word_dict = {}
    for i in range(1,L+1):
        word = input()
        int_dict[i] = word
        word_dict[word]= i


    q_list = [ input() for i in range(M)]


    for q in q_list:

        if q.isdigit():
            print(int_dict[int(q)])
        else:
            print(word_dict[q])


solution()