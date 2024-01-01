import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    buff = input().split()

    if buff[0] == "push":
        q.append(buff[1])
    elif buff[0] == "pop":
        print(q.popleft()) if q else print(-1)
    elif buff[0] == "size":
        print(len(q))
    elif buff[0] == "empty":
        print(0) if q else print(1)
    elif buff[0] == "front":
        print(q[0]) if q else print(-1)
    else:
        print(q[-1]) if q else print(-1)
