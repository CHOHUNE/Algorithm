from itertools import combinations

aeiou =['a','e','i','o','u']

def is_possible(word):
    global a,b,L
    num=0
    for w in word:
        num += w in aeiou
    etc = a-num
    return etc>=2 and num>=1 

a,b = map(int,input().split())
L = input().split()
L.sort()

for comb in combinations(L,a):
    if is_possible(comb):
        print(''.join(comb))
