import sys

input = sys.stdin.readline

def solution():

    N = int(input())

    first_row = list(map(int,input().split()))
    dp_max= first_row[:]
    dp_min = first_row[:]
    

    for _ in range(N-1):

        row = list(map(int,input().split()))

        new_max = [0] * 3
        new_min = [0] * 3 

        for j in range(3):

            candidate_max = []
            candidate_min = []

            for prev_j in range(max(0,j-1),min(3,j+2)):

                candidate_max.append(dp_max[prev_j])
                candidate_min.append(dp_min[prev_j])

            new_max[j] = row[j] + max(candidate_max)
            new_min[j] = row[j] + min(candidate_min)

        dp_max = new_max
        dp_min = new_min

    print(max(dp_max),min(dp_min),sep= ' ')

solution()