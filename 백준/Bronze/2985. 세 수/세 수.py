def solution():
    N = list(map(int, input().split()))
    if N[0] + N[1] == N[2]:
        print(f"{N[0]}+{N[1]}={N[2]}")
    elif N[0] - N[1] == N[2]:
        print(f"{N[0]}-{N[1]}={N[2]}")
    elif N[0] * N[1] == N[2]:
        print(f"{N[0]}*{N[1]}={N[2]}")
    elif N[0] / N[1] == N[2]:
        print(f"{N[0]}/{N[1]}={N[2]}")
    elif N[0] == N[1] + N[2]:
        print(f"{N[0]}={N[1]}+{N[2]}")
    elif N[0] == N[1] - N[2]:
        print(f"{N[0]}={N[1]}-{N[2]}")
    elif N[0] == N[1] * N[2]:
        print(f"{N[0]}={N[1]}*{N[2]}")
    elif N[0] == N[1] / N[2]:
        print(f"{N[0]}={N[1]}/{N[2]}")

solution()