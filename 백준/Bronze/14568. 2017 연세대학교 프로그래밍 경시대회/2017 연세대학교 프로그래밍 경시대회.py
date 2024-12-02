def solution ():
	n= int(input())
	cnt=0
	for A in range(0,n+1):
		for B in range(0,n+1):
			for C in range(0,n+1):
				if A+B+C == n:
					if A>=B+2 :
						if C%2==0:
							if A!=0 and B!=0 and C!=0 :
								cnt+=1
	print(cnt)
solution()
