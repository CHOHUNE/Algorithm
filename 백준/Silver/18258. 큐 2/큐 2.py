import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    n = int(input())
    queue = deque()
    results = []
    
    for _ in range(n):
        cmd = input().split()
        
        if cmd[0] == "push":
            queue.append(cmd[1])
        elif cmd[0] == "pop":
            results.append(str(queue.popleft()) if queue else "-1")
        elif cmd[0] == "size":
            results.append(str(len(queue)))
        elif cmd[0] == "empty":
            results.append("1" if not queue else "0")
        elif cmd[0] == "front":
            results.append(str(queue[0]) if queue else "-1")
        else:  # back
            results.append(str(queue[-1]) if queue else "-1")
    
    print('\n'.join(results))

solution()