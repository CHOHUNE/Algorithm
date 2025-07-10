import sys
input = lambda : sys.stdin.readline().rstrip()

def solution():

	N = int(input())
	X = []

	for i in range(N):
		x,y = map(int,input().split())
		X.append((x,y))


	X = sorted(X)

	for x,y in X:
		print(x,y)

solution()