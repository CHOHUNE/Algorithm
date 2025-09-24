import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    for i in range(N):
        word = input().strip()
        ans = []
        for char in word:
            if char == '(':
                ans.append(char)
            elif char == ')':
                if ans != []:
                    ans.pop()
                else:
                    print("NO")
                    break
        else:
        
            if ans == []:
                print("YES")
            else:
                print("NO")
        
            
solution()
                
            