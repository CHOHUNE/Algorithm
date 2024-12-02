def solution():
  n = int(input())
  for _ in range(n):
    value = int(input())
    for i in range(2,1_000_001):
      if value % i ==0 : 
        print("NO")
        break
      if i == 1_000_000:
        print("YES")

        
solution()