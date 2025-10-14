import sys

input = sys.stdin.readline

def solution():
    N = int(input())


    ans = set()
    for i in range(N):

        each =  input().split() 

        if each[0] == "add":
            ans.add(each[1])
        elif each[0] == "remove" and each[1] in ans:
            ans.remove(each[1])
        elif each[0] == "check":
            if each[1] in ans:
                print(1)
            else:
                print(0)
        elif each[0] == "toggle":
            if each[1] in ans:
                ans.remove(each[1])
            else:
                ans.add(each[1])
        elif each[0] == "all":
            ans = {str(i) for i in range(1,21)}

        elif each[0] =="empty":
            ans =set()


solution()    