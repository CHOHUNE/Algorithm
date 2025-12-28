import sys

input = sys.stdin.readline

def solution():


    N = int(input())
    M = int(input()) #length

    pattern = 'I'+('OI' * N) 
    ans = 0
    parse = input().strip()

    for i in range(M):

        if parse[i:i+len(pattern)] == pattern:

            ans += 1 


    print(ans)


solution()