def solution():
  a,b = map(int,input().split())
  num_list = list(map(int,input().split()))

  ans=[]
  for x in range(len(num_list)-2):
    for y in range(x+1,len(num_list)-1):
      for z in range(y+1,len(num_list)):
        current_num= num_list[x]+num_list[y]+num_list[z]
        if current_num <= b:
          ans.append(current_num)
  ans=sorted(ans)
  print(ans[-1])

solution()



