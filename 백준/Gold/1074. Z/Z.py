import sys

input =sys.stdin.readline


def solve(n,row,col):

    if n == 0:
        return 0
    half = 2 ** (n-1)
    area = half * half 
    
    if row < half and col < half :
        
        return solve(n-1,row,col)
    
    elif row < half and col >= half :
        return area + solve(n-1,row,col-half)
    
    elif row >= half and col < half :
        return area*2 + solve(n-1, row-half,col)
    
    elif row >= half and col >= half:
        return area*3  + solve(n-1, row-half , col-half)
    
def solution():

    N,row,col = map(int,input().split())
    print(solve(N,row,col))


solution()
