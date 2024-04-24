import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
d = deque()

for _ in range(n):
    buff = input().split()

    if buff[0] == "push_front":
        d.appendleft(int(buff[1]))
    elif buff[0] == "push_back":
        d.append(int(buff[1]))
    elif buff[0] == "pop_front":
        print(d.popleft()) if d else print(-1)
    elif buff[0] == "pop_back":
        print(d.pop()) if d else print(-1)
    elif buff[0] == "size":
        print(len(d))
    elif buff[0] == "empty":
        print(0) if d else print(1)
    elif buff[0] == "front":
        print(d[0]) if d else print(-1)
    else:
        print(d[-1]) if d else print(-1)
